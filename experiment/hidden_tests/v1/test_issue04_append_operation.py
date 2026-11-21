"""Hidden acceptance tests for issue 04 (operations.append)."""
import pytest
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from tinydb.operations import append

Q = Query()


def test_append_to_existing_list():
    db = TinyDB(storage=MemoryStorage)
    db.insert({'id': 3, 'tags': ['a']})
    db.update(append('tags', 'urgent'), Q.id == 3)
    assert db.get(Q.id == 3)['tags'] == ['a', 'urgent']


def test_append_creates_missing_field():
    db = TinyDB(storage=MemoryStorage)
    db.insert({'id': 3})
    db.update(append('tags', 'urgent'), Q.id == 3)
    assert db.get(Q.id == 3)['tags'] == ['urgent']


def test_append_non_list_raises_type_error():
    db = TinyDB(storage=MemoryStorage)
    db.insert({'id': 3, 'tags': 'oops'})
    with pytest.raises(TypeError):
        db.update(append('tags', 'urgent'), Q.id == 3)


def test_append_only_matching_documents():
    db = TinyDB(storage=MemoryStorage)
    db.insert_multiple([{'id': 1, 'tags': []}, {'id': 2, 'tags': []}])
    db.update(append('tags', 'x'), Q.id == 2)
    assert [d['tags'] for d in db.all()] == [[], ['x']]
