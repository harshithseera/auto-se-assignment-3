"""Hidden acceptance tests for T3 (batched writes via TinyDB.batch())."""
import json

import pytest

from tinydb import TinyDB, Query
from tinydb.middlewares import CachingMiddleware
from tinydb.storages import JSONStorage, MemoryStorage


class SpyStorage(MemoryStorage):
    def __init__(self):
        super().__init__()
        self.writes = 0

    def write(self, data):
        self.writes += 1
        super().write(data)


def test_batch_writes_once_across_tables():
    db = TinyDB(storage=SpyStorage)
    spy = db.storage
    db.insert({'a': 1})
    logs = db.table('logs')
    logs.insert({'id': 3, 'seen': False})
    before = spy.writes

    with db.batch():
        db.insert({'a': 2})
        db.insert_multiple([{'a': 3}, {'a': 4}])
        db.update({'b': True}, Query().a == 1)
        logs.update({'seen': True}, Query().id == 3)
        db.remove(Query().a == 4)

    assert spy.writes == before + 1
    assert sorted(d['a'] for d in db.all()) == [1, 2, 3]
    assert db.get(Query().a == 1) == {'a': 1, 'b': True}
    assert logs.all() == [{'id': 3, 'seen': True}]
    assert spy.read()['logs'] == {'1': {'id': 3, 'seen': True}}

    with db.batch():
        db.search(Query().a == 1)
        len(db)
    assert spy.writes == before + 1


def test_reads_inside_batch_see_pending_changes():
    db = TinyDB(storage=SpyStorage)
    db.insert({'a': 1})
    Q = Query()
    assert db.count(Q.a == 1) == 1  # populate the query cache

    with db.batch():
        new_id = db.insert({'a': 1, 'new': True})
        assert db.count(Q.a == 1) == 2
        assert len(db.search(Q.a == 1)) == 2
        assert db.get(doc_id=new_id) == {'a': 1, 'new': True}
        assert db.contains(Q.new == True)  # noqa: E712
        assert len(db) == 2
        assert len(db.all()) == 2
        assert len(list(iter(db))) == 2
        db.truncate()
        assert len(db) == 0
        db.insert({'z': 1})
        assert db.all() == [{'z': 1}]

    assert db.all() == [{'z': 1}]


def test_exception_rolls_everything_back():
    db = TinyDB(storage=SpyStorage)
    spy = db.storage
    db.insert_multiple([{'a': 1}, {'a': 2}])
    other = db.table('other')
    other.insert({'o': 1})
    Q = Query()
    assert db.search(Q.a == 1) == [{'a': 1}]  # populate the query cache
    snapshot = json.loads(json.dumps(spy.read()))
    writes_before = spy.writes

    with pytest.raises(ZeroDivisionError):
        with db.batch():
            db.insert({'a': 1})
            db.insert({'a': 9})
            db.update({'a': 100}, Q.a == 2)
            other.remove(Q.o == 1)
            db.table('fresh').insert({'f': 1})
            assert len(db.search(Q.a == 1)) == 2
            1 / 0

    assert spy.writes == writes_before
    assert spy.read() == snapshot
    assert db.search(Q.a == 1) == [{'a': 1}]
    assert db.count(Q.a == 100) == 0
    assert other.all() == [{'o': 1}]
    assert db.table('fresh').all() == []
    assert db.insert({'a': 3}) == 3
    assert other.insert({'o': 2}) == 2


def test_nested_batches_and_other_storages(tmp_path):
    db = TinyDB(storage=SpyStorage)
    spy = db.storage
    with db.batch():
        db.insert({'x': 1})
        with db.batch():
            db.insert({'x': 2})
        assert spy.writes == 0
        db.insert({'x': 3})
    assert spy.writes == 1
    assert [d['x'] for d in db.all()] == [1, 2, 3]

    path = tmp_path / 'db.json'
    jdb = TinyDB(str(path), storage=JSONStorage)
    jdb.insert({'j': 1})
    with jdb.batch():
        jdb.insert({'j': 2})
        jdb.table('t').insert({'t': 1})
    with pytest.raises(RuntimeError):
        with jdb.batch():
            jdb.insert({'j': 3})
            raise RuntimeError('boom')
    jdb.close()
    on_disk = json.loads(path.read_text())
    assert on_disk == {'_default': {'1': {'j': 1}, '2': {'j': 2}},
                       't': {'1': {'t': 1}}}

    cdb = TinyDB(storage=CachingMiddleware(SpyStorage))
    inner = cdb.storage.storage
    with cdb.batch():
        cdb.insert({'c': 1})
        cdb.insert({'c': 2})
        assert cdb.count(Query().c.exists()) == 2
    with pytest.raises(KeyError):
        with cdb.batch():
            cdb.insert({'c': 3})
            raise KeyError('x')
    assert [d['c'] for d in cdb.all()] == [1, 2]
    cdb.close()
    assert inner.writes == 1
    assert inner.memory == {'_default': {'1': {'c': 1}, '2': {'c': 2}}}
