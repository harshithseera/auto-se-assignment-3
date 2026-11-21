"""Hidden acceptance tests for issue 05 (vague: storing datetimes).

Interpretation tested: inserting a datetime into the default JSON storage must not
fail, and the value must round-trip either as an equal ``datetime`` or as its ISO-8601
string. Either design choice passes.
"""
from datetime import datetime, date
from tinydb import TinyDB, Query

WHEN = datetime(2024, 3, 15, 10, 30, 0)


def _ok(value, original):
    return value == original or value == original.isoformat()


def test_insert_datetime_does_not_raise(tmp_path):
    db = TinyDB(tmp_path / 'db.json')
    db.insert({'title': 'hello', 'created': WHEN})
    db.close()


def test_datetime_round_trips_after_reopen(tmp_path):
    path = tmp_path / 'db.json'
    with TinyDB(path) as db:
        db.insert({'title': 'hello', 'created': WHEN})
    with TinyDB(path) as db:
        assert _ok(db.all()[0]['created'], WHEN)


def test_date_round_trips(tmp_path):
    path = tmp_path / 'db.json'
    with TinyDB(path) as db:
        db.insert({'d': date(2024, 3, 15)})
    with TinyDB(path) as db:
        assert _ok(db.all()[0]['d'], date(2024, 3, 15))


def test_plain_documents_unaffected(tmp_path):
    path = tmp_path / 'db.json'
    with TinyDB(path) as db:
        db.insert({'title': 'hello', 'n': 1})
    with TinyDB(path) as db:
        assert db.search(Query().n == 1) == [{'title': 'hello', 'n': 1}]
