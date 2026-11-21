"""Hidden acceptance tests for issue 01 (search results must not alias the query cache)."""
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

Q = Query()


def _db():
    db = TinyDB(storage=MemoryStorage)
    db.insert({'name': 'theme', 'value': 'light'})
    return db


def test_mutating_result_does_not_change_next_search():
    db = _db()
    db.search(Q.name == 'theme')[0]['value'] = 'dark'
    assert db.search(Q.name == 'theme') == [{'name': 'theme', 'value': 'light'}]


def test_search_agrees_with_all_after_local_edit():
    db = _db()
    db.search(Q.name == 'theme')[0]['value'] = 'dark'
    assert db.search(Q.name == 'theme') == db.all()


def test_adding_key_to_result_does_not_leak():
    db = _db()
    db.search(Q.name == 'theme')[0]['extra'] = 1
    assert 'extra' not in db.search(Q.name == 'theme')[0]


def test_update_still_visible_to_search():
    db = _db()
    db.search(Q.name == 'theme')
    db.update({'value': 'dark'}, Q.name == 'theme')
    assert db.search(Q.name == 'theme')[0]['value'] == 'dark'
