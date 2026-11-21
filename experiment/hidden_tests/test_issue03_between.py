"""Hidden acceptance tests for issue 03 (Query.between, inclusive)."""
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

Q = Query()


def _db():
    db = TinyDB(storage=MemoryStorage)
    db.insert_multiple([{'age': a} for a in (17, 18, 25, 30, 31)] + [{'name': 'no age'}])
    return db


def test_between_is_inclusive():
    assert [d['age'] for d in _db().search(Q.age.between(18, 30))] == [18, 25, 30]


def test_between_missing_field_does_not_match():
    assert all('age' in d for d in _db().search(Q.age.between(0, 100)))


def test_between_combines_and_strings():
    db = _db()
    assert [d['age'] for d in db.search(~Q.age.between(18, 30) & Q.age.exists())] == [17, 31]
    db.insert({'day': '2024-03-15'})
    assert len(db.search(Q.day.between('2024-01-01', '2024-12-31'))) == 1


def test_between_different_bounds_not_cached_together():
    db = _db()
    assert len(db.search(Q.age.between(18, 30))) == 3
    assert len(db.search(Q.age.between(17, 18))) == 2
