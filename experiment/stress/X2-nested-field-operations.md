# Update operations only work on top-level fields

`increment`, `set`, `delete` and the other helpers in `tinydb.operations` only take a top-level field name. Most of my documents are nested, e.g. `{'address': {'city': ...}, 'stats': {'visits': 3}}`, so I keep writing my own little functions for things like bumping `stats.visits`.

Could the operations accept a path instead? Something like:

```python
db.update(set(('address', 'city'), 'Pune'))
db.update(increment(['stats', 'visits']))
```

What I'd expect:
- a plain string should keep working exactly like today, even if it has a dot in it (I do have keys like `'a.b'`)
- `set` should create missing dicts along the way, the other ones should raise `KeyError` if something on the path is missing, same as they do now for a missing field
- if something along the path isn't a dict (say `n` is `5` and I ask for `('n', 'x')`) I'd want a `TypeError`, and the document shouldn't be half-changed
