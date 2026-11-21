# Shortcut for range queries?

I do a lot of "between X and Y" searches and always end up writing

```python
db.search((Query().age >= 18) & (Query().age <= 30))
```

Would be really nice to have something like `Query().age.between(18, 30)` that gives me everyone from 18 to 30, with 18 and 30 themselves included. I'd also use it for dates I store as strings like `'2024-03-15'`. People without an age shouldn't show up, same as with the normal comparisons.
