# Feature request: `append` operation for list fields

**Type:** feature

`tinydb.operations` has `add`, `increment`, `set` etc., but nothing for lists. To add a tag to a document I currently have to read it, change the list and write the whole field back. I'd like:

```python
from tinydb.operations import append

db.update(append('tags', 'urgent'), Query().id == 3)
```

- If `tags` is a list, `'urgent'` is added to the end.
- If the document has no `tags` field yet, it should be created as `['urgent']`.
- If `tags` exists but isn't a list, I'd expect a `TypeError` rather than silently replacing my data.
