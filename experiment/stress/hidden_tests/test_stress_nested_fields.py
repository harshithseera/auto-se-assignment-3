"""Hidden acceptance tests for T2 (nested fields in update operations)."""
import pytest

from tinydb import TinyDB
from tinydb.operations import add, decrement, delete, increment, set, subtract
from tinydb.storages import MemoryStorage


def _db(doc):
    db = TinyDB(storage=MemoryStorage)
    db.insert(doc)
    return db


def test_set_creates_missing_parents_and_keeps_siblings():
    db = _db({'name': 'x', 'address': {'zip': '1'}})
    db.update(set(('address', 'city'), 'Pune'))
    db.update(set(['meta', 'tags', 'main'], 'db'))
    assert db.all()[0] == {
        'name': 'x',
        'address': {'zip': '1', 'city': 'Pune'},
        'meta': {'tags': {'main': 'db'}},
    }


def test_arithmetic_and_delete_on_nested_paths():
    db = _db({'stats': {'visits': 1, 'score': 10, 'label': 'a', 'tmp': 0}})
    db.update(increment(['stats', 'visits']))
    db.update(decrement(('stats', 'score')))
    db.update(add(('stats', 'score'), 5))
    db.update(subtract(['stats', 'visits'], 3))
    db.update(add(('stats', 'label'), 'b'))
    db.update(delete(('stats', 'tmp')))
    assert db.all()[0] == {'stats': {'visits': -1, 'score': 14, 'label': 'ab'}}


def test_missing_keys_and_non_dict_values_raise():
    doc = {'a': {'b': 1}, 'n': 5}
    for op in (increment(('a', 'missing')), increment(('nope', 'b')),
               delete(('a', 'missing')), add(['nope', 'x'], 1)):
        with pytest.raises(KeyError):
            op(dict(doc, a=dict(doc['a'])))

    for op in (set(('n', 'x'), 1), increment(('n', 'x'))):
        with pytest.raises(TypeError):
            op(dict(doc, a=dict(doc['a'])))

    db = _db({'n': 5})
    with pytest.raises(TypeError):
        db.update(set(('n', 'x'), 1))
    assert db.all()[0] == {'n': 5}


def test_plain_string_fields_keep_their_meaning():
    db = _db({'a.b': 1, 'a': {'b': 100}, 'c': 1})
    db.update(increment('a.b'))
    db.update(set('new.key', 'v'))
    db.update(add('c', 2))
    db.update(delete('c'))
    assert db.all()[0] == {'a.b': 2, 'a': {'b': 100}, 'new.key': 'v'}
