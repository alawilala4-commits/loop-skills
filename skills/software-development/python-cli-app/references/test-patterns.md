# Common Test Patterns for Python CLI Apps

## Mocking `input()` for interactive commands

When a function uses `input()` in a validation loop, mock it with `side_effect`:

```python
@patch("builtins.input", side_effect=["a", "b"])
def test_command(self, mock_input):
    result = run_interactive(...)
    self.assertEqual(result["total"], 2)
```

For input validation loops, include invalid inputs before valid ones:

```python
@patch("builtins.input", side_effect=["invalid", "a"])
def test_invalid_then_valid(self, mock_input):
    result = run_interactive(...)
    self.assertEqual(result["total"], 1)
```

## Mocking `random.shuffle` for deterministic order

```python
@patch("module.random.shuffle", lambda x: None)
def test_deterministic(self):
    # items stay in insertion order
    result = get_items()
    self.assertEqual(result[0]["id"], 1)
```

## Mocking `time.time()` / clock-based logic

Extract `_now()` in the app code so it's patchable:

```python
# In app code:
def _now():
    return time.time()

# In tests:
@patch("module._now", return_value=1010.0)
def test_timer(self, mock_now):
    ...
```

For multiple sequential time calls, use `side_effect`:

```python
@patch("module._now", side_effect=[1000.0, 1010.0, 1020.0])
def test_sequential(self, mock_now):
    ...
```

## JSON persistence roundtrip

Always use `tempfile` for isolation:

```python
with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
    path = f.name
try:
    save_data(self.items, path)
    loaded = load_data(path)
    self.assertEqual(len(loaded), expected)
    self.assertEqual(loaded[0]["field"], "value")
finally:
    os.unlink(path)
```

## Multiple `@patch` decorators

Decorator order is bottom-up, parameters reverse. Prefer context managers:

```python
def test_something(self):
    with patch("builtins.input", side_effect=["a"]):
        with patch("module.random.shuffle", lambda x: None):
            result = function_under_test(...)
            self.assertEqual(result["total"], 1)
```

## Rounding pitfalls

Python's `round()` uses banker's rounding (round half to even):

```python
round(100.0 + 0.005, 2)  # = 100.0 (not 100.01!)
round(100.0 + 0.006, 2)  # = 100.01
```

Use 0.006+ when testing that values round up to the next cent.
