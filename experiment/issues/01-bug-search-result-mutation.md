# Changing a search result changes what the next search returns

**Type:** bug

I'm using TinyDB to keep some settings and noticed something weird. If I search, then change one of the returned documents locally (without calling `update`), the *next* search for the same thing gives me my local change back, even though I never saved it:

```python
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

db = TinyDB(storage=MemoryStorage)
db.insert({'name': 'theme', 'value': 'light'})

Setting = Query()
result = db.search(Setting.name == 'theme')
result[0]['value'] = 'dark'          # just a local edit, not saved

print(db.search(Setting.name == 'theme'))
# [{'name': 'theme', 'value': 'dark'}]   <-- expected 'light'
print(db.all())
# [{'name': 'theme', 'value': 'light'}]  <-- this one is right
```

So `search` and `all` disagree about what's in the database. I'd expect search results to be my own copy, like `all()` seems to be, and the database to only change when I call `update`.

TinyDB version: current master.
