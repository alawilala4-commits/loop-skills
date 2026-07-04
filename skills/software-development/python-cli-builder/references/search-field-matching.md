# Search Field Matching Pitfall

When a `search_*` function searches across multiple fields (e.g., title AND content, name AND description), a single keyword can match **multiple entries across different fields**. This causes test assertion failures when you expect 1 result but get 2.

## Example

```python
entries = [
    {"title": "Python Basics", "content": "Learned variables"},      # matches via title
    {"title": "Cooking", "content": "Made pasta"},                    # no match
    {"title": "Travel", "content": "Python scripts for travel"},      # matches via content
]
search_entries(entries, "python")  # returns 2, not 1!
```

## The Fix

Before asserting a count, trace which entries actually match:
1. Check which entries have the keyword in field A
2. Check which entries have the keyword in field B
3. Sum the unique matches
4. Assert on that sum

## Pattern

```python
def test_search_title(self):
    results = search_entries(self.entries, "python")
    # "Python" in entry 1 title, "Python" in entry 3 content
    self.assertEqual(len(results), 2)
```

## Projects Where This Bit

- journal.py: search_entries searches title + content
- quiz.py: search_courses searches name + code + instructor
- library.py: search_books searches title + author + ISBN
- course.py: search_courses searches name + code + instructor
- school.py: search_students searches name + class
