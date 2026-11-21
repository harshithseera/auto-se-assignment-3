# `Query() < value` crashes the whole search if one document has a different type

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

Same with `<=`, `>` and `>=`. Documents that don't have a `price` at all are skipped fine, so I'd expect the `"TBD"` one to just not match too, and get back only the pen.
