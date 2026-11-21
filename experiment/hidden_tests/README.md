# Hidden acceptance tests

These are kept outside the fork, so agents never see them. File `test_issue0K_*.py` belongs to issue slot K:

| Slot | Fork issue | Type | File |
|---|---|---|---|
| 01 | #16 | bug | `test_issue01_drop_table_stale_search.py` |
| 02 | #17 | bug | `test_issue02_mixed_type_comparison.py` |
| 03 | #18 | feature | `test_issue03_between.py` |
| 04 | #19 | feature | `test_issue04_append_operation.py` |
| 05 | #20 | vague | `test_issue05_dates.py` |

To score a PR:

```bash
cd tinydb && git checkout autose/issue-N
cp ../auto-se-assignment-3/experiment/hidden_tests/test_issue0K_*.py tests/
python -m pytest tests/test_issue0K_*.py -p no:cacheprovider --no-cov -q
git checkout -- tests && git clean -fd tests
```

Results on the pinned base `edff96a`: 14 tests fail, and `test_issue04_*` fails to import because `append` does not exist yet. Two tests pass on the base on purpose, as regression guards: `test_issue01::test_reinsert_after_drop_returns_only_new_documents` and `test_issue05::test_documents_without_dates_unaffected`.

`v1/` holds the tests for the first issue set (#1–#5). The v1 slot 01 described behaviour that was documented as intended at `edff96a` (search results share objects with the query cache; see `docs/usage.rst`), so it was replaced with a genuine, undocumented bug.
