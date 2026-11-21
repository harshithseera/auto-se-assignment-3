"""Hidden acceptance tests for issue 01 (dropped tables must not serve cached results)."""
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

U = Query()


def _setup():
    db = TinyDB(storage=MemoryStorage)
    users = db.table('users')
    users.insert({'name': 'ann'})
    assert users.search(U.name == 'ann') == [{'name': 'ann'}]  # warm the cache
    return db, users


def test_search_after_drop_table_is_empty():
    db, users = _setup()
    db.drop_table('users')
    assert users.search(U.name == 'ann') == []


def test_count_after_drop_table_is_zero():
    db, users = _setup()
    db.drop_table('users')
    assert users.count(U.name == 'ann') == 0


def test_search_after_drop_tables_is_empty():
    db, users = _setup()
    db.drop_tables()
    assert users.search(U.name == 'ann') == []


def test_reinsert_after_drop_returns_only_new_documents():
    db, users = _setup()
    db.drop_table('users')
    users.insert({'name': 'bob'})
    assert users.search(U.name == 'ann') == []
    assert [d['name'] for d in users.search(U.name.exists())] == ['bob']
