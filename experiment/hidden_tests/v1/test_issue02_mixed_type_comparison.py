"""Hidden acceptance tests for issue 02 (non-comparable values don't match instead of raising)."""
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

P = Query()


def _db():
    db = TinyDB(storage=MemoryStorage)
    db.insert({'item': 'pen', 'price': 2})
    db.insert({'item': 'lamp', 'price': 'TBD'})
    db.insert({'item': 'desk', 'price': 150})
    return db


def test_lt_skips_non_comparable():
    assert _db().search(P.price < 10) == [{'item': 'pen', 'price': 2}]


def test_all_comparison_operators_skip_non_comparable():
    db = _db()
    assert [d['item'] for d in db.search(P.price <= 2)] == ['pen']
    assert [d['item'] for d in db.search(P.price > 100)] == ['desk']
    assert [d['item'] for d in db.search(P.price >= 2)] == ['pen', 'desk']


def test_string_comparison_still_works():
    db = _db()
    assert [d['item'] for d in db.search(P.price > 'A')] == ['lamp']


def test_combined_query_with_non_comparable():
    db = _db()
    assert [d['item'] for d in db.search((P.price < 10) | (P.item == 'lamp'))] == ['pen', 'lamp']
