"""Hidden acceptance tests for issue 05 (vague: "support for dates").

Interpretation tested (the minimum any reasonable reading needs): date and datetime
values can be saved to the default JSON file storage and read back after reopening,
either as equal date/datetime objects or as their ISO-8601 strings.
"""
from datetime import datetime, date
from tinydb import TinyDB, Query

WHEN = datetime(2024, 3, 15, 10, 30, 0)
DAY = date(2024, 3, 15)


def _ok(value, original):
    return value == original or value == original.isoformat()


def test_saving_datetime_to_file_does_not_raise(tmp_path):
    with TinyDB(tmp_path / 'db.json') as db:
        db.insert({'title': 'hello', 'created': WHEN})


def test_datetime_round_trips_after_reopen(tmp_path):
    path = tmp_path / 'db.json'
    with TinyDB(path) as db:
        db.insert({'title': 'hello', 'created': WHEN})
    with TinyDB(path) as db:
        assert _ok(db.all()[0]['created'], WHEN)


def test_date_round_trips_after_reopen(tmp_path):
    path = tmp_path / 'db.json'
    with TinyDB(path) as db:
        db.insert({'due': DAY})
    with TinyDB(path) as db:
        assert _ok(db.all()[0]['due'], DAY)


def test_documents_without_dates_unaffected(tmp_path):
    path = tmp_path / 'db.json'
    with TinyDB(path) as db:
        db.insert({'title': 'hello', 'n': 1})
    with TinyDB(path) as db:
        assert db.search(Query().n == 1) == [{'title': 'hello', 'n': 1}]
