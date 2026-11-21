# Dates don't work

**Type:** unclear

I tried storing when each entry was created and TinyDB just crashes:

```python
from datetime import datetime
from tinydb import TinyDB

db = TinyDB('db.json')
db.insert({'title': 'hello', 'created': datetime.now()})
```

Pretty much every app needs dates. Can TinyDB support them?
