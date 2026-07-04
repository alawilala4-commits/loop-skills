# unittest.mock.patch Ordering Pitfall

When stacking multiple `@patch` decorators on a test method, mock parameters are passed in **reverse order** — the bottom decorator becomes the first parameter. This is a common source of `TypeError: missing 1 required positional argument` errors.

## The Bug

```python
@patch("builtins.input", side_effect=["a", "b"])      # 2nd param
@patch("quiz.random.shuffle", lambda x: None)          # 1st param
def test_run_all_correct(self, mock_input, mock_shuffle):  # WRONG order
    ...
```

The parameters are `(mock_shuffle, mock_input)` not `(mock_input, mock_shuffle)`.

## The Fix

**Prefer `with` context managers** — they're clearer and avoid parameter ordering bugs entirely:

```python
def test_run_all_correct(self):
    with patch("builtins.input", side_effect=["a", "b"]):
        with patch("quiz.random.shuffle", lambda x: None):
            from quiz import run_quiz
            result = run_quiz(self.qs, limit=2)
            self.assertEqual(result["total"], 2)
```

## When You Must Use Stacked Decorators

If you must stack (e.g., for `side_effect` on `input`), remember: **bottom decorator = first parameter**. Add a comment:

```python
@patch("builtins.input", side_effect=["a", "b"])      # → 2nd param
@patch("quiz.random.shuffle", lambda x: None)          # → 1st param
def test_run_all_correct(self, mock_shuffle, mock_input):  # note: reversed
    ...
```

But the `with` approach is strongly preferred.
