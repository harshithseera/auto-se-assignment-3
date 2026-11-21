# Dropped table still returns old documents from search()

I keep a handle to each table around (`users = db.table('users')`) and reset things with `drop_table` in my tests. After dropping, `search` on my handle still gives me the old documents back, even though `all()` and `len()` say the table is empty:

```python
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

db = TinyDB(storage=MemoryStorage)
users = db.table('users')
users.insert({'name': 'ann'})

User = Query()
users.search(User.name == 'ann')   # [{'name': 'ann'}]

db.drop_table('users')

print(users.all())                 # []
print(len(users))                  # 0
print(users.search(User.name == 'ann'))   # [{'name': 'ann'}]  <-- still there?!
```

Same thing happens with `db.drop_tables()`. I'd expect a dropped table to really be empty, including for searches I already ran before dropping it.
