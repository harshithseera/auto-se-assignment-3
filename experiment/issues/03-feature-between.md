# Feature request: `between()` for range queries

**Type:** feature

Range queries currently need two conditions combined with `&`:

```python
db.search((Query().age >= 18) & (Query().age <= 30))
```

That's a lot of typing for something I do all the time. Could we get a `between` method on queries?

```python
db.search(Query().age.between(18, 30))
```

It should include both ends (18 and 30 both match), work on anything comparable (numbers, strings, dates stored as ISO strings), and documents without the field should just not match, like the other query methods. It should of course combine with `&`, `|` and `~` like any other query.
