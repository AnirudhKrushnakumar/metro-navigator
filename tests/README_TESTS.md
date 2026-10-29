# Metro Navigator student unit tests

These are **tests only**. They are not the implementations of the eight required data structures. Put the `tests` folder in the root of your `metro-navigator` repository, next to `linked_list.py`, `hash_table.py`, `bst.py`, `min_heap.py`, `graph.py`, `linked_stack.py`, `linked_queue.py`, and `hash_set.py`.

Your repository should include:

```text
metro-navigator/
  linked_list.py
  hash_table.py
  bst.py
  min_heap.py
  graph.py
  linked_stack.py
  linked_queue.py
  hash_set.py
  tests/
    __init__.py
    test_linked_list.py
    test_hash_table.py
    test_bst.py
    test_min_heap.py
    test_graph.py
    test_stack.py
    test_queue.py
    test_hash_set.py
    test_integration.py
```

Run the tests from the repository root, using the project-required command:

```bash
python -m unittest discover -s tests -t .
```

To run one file while you are developing, for example:

```bash
python -m unittest tests.test_linked_list
```

## What to expect

- Tests will fail until the matching implementation files and methods exist. Import errors usually mean a required file, class, method, or import name is missing or spelled differently.
- The tests follow the **unweighted graph** version of the assignment. `Graph.add_edge(u, v)` takes two station names and `neighbors(name)` returns station-name strings, not `(station, weight)` pairs. Edge tuples in `edges()` are `(u, v)` pairs.
- The MinHeap is tested separately with numeric maintenance-task priorities. These are not graph-edge weights.
- The test files use Python built-ins such as `dict` and `set` only as test-side reference models. The implementation files must still obey the project's restrictions.
- A passing test suite is necessary but not sufficient. You must also meet the implementation design constraints, GitHub requirements, documentation requirements, and the `main.py` demonstration requirements in the project brief.

## Test IDs

Each official project check has its own `unittest` method using the naming pattern `test_LL_01`, `test_HT_01`, `test_BST_01`, `test_MH_01`, `test_G_01`, `test_ST_01`, `test_QU_01`, `test_SET_01`, or `test_INT_01`. The `EXTRA` tests provide additional coverage beyond the listed checks.
