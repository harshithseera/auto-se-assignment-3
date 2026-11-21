# Add an operation to append to a list field

There's `add`, `increment`, `set` and friends in `tinydb.operations`, but nothing for lists, so adding a tag means reading the document, changing the list and writing it back. I'd love to just do:

```python
from tinydb.operations import append

db.update(append('tags', 'urgent'), Query().id == 3)
```

If the document doesn't have `tags` yet it'd be great if it just started a new list. And if `tags` is something other than a list, please raise a `TypeError` rather than quietly overwriting what's there.
