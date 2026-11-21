# Way to group several writes into one?

I'm using a JSON file and doing a bunch of inserts/updates in a row, across a couple of tables. Every single call rewrites the whole file, which is slow, and if something fails halfway I end up with half my changes saved.

Would love something like:

```python
with db.batch():
    db.insert({'a': 1})
    db.table('logs').update({'seen': True}, Query().id == 3)
```

where everything inside the block is written to storage once at the end (and not at all if nothing changed). Searches and counts inside the block should already see the changes I made in it. If an exception happens inside the block, nothing should be written and the database should behave as if the block never ran, including which IDs new documents get afterwards. A `batch()` inside another `batch()` can just be part of the outer one. It should work with any storage, also `CachingMiddleware`.
