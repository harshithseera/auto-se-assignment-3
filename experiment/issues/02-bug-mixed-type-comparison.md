# `Query() < value` crashes the whole search if one document has a different type

**Type:** bug

I have a table of products where `price` is normally a number, but a few old entries have `price` stored as a string like `"TBD"`. Any comparison query now blows up instead of just skipping those entries:

```python
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

db = TinyDB(storage=MemoryStorage)
db.insert({'item': 'pen', 'price': 2})
db.insert({'item': 'lamp', 'price': 'TBD'})
db.insert({'item': 'desk', 'price': 150})

Product = Query()
db.search(Product.price < 10)
# TypeError: '<' not supported between instances of 'str' and 'int'
```

Same with `<=`, `>` and `>=`. Missing fields are already handled nicely (documents without `price` are just not matched), so I'd expect a value that can't be compared to behave the same way: the document doesn't match, and I get `[{'item': 'pen', 'price': 2}]`.

TinyDB version: current master.
