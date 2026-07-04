# Multi-Entity App Pattern

For apps managing multiple entity types (school, clinic, CRM, library), use a single JSON file with top-level keys per entity.

## Data Structure

```json
{
  "students": [...],
  "teachers": [...],
  "appointments": [...]
}
```

Each entity has: `id`, domain fields, `created_at`, and optionally sub-entity lists (notes, enrollments).

## File Layout

```
~/projects/<name>/
├── <name>.py          # All entities + cross-entity operations in one file
├── test_<name>.py     # Tests organized by entity class
└── <name>_data.json   # Single JSON file with all data
```

## Test Organization

Group tests by entity:
- `TestStudents` — add, delete, list, search
- `TestTeachers` — add, delete, list
- `TestEnrollments` / `TestAppointments` — cross-entity operations
- `TestIntegration` — full workflow across entities

## Cross-Entity Operations

Functions like `enroll_student()`, `book_appointment()`, `add_note()`:
1. Validate both entities exist (by ID)
2. Check business rules (not already enrolled, not already booked)
3. Update both entities atomically
4. Return the modified parent entity

## Pitfall: Test setUp for Multi-Entity Tests

When tests need multiple entities, add them in each test (not in setUp) unless all tests need the same setup. For cross-entity tests, always add both entities:

```python
def setUp(self):
    self.data = _fresh()

def test_book_appointment(self):
    add_patient(self.data["patients"], "Alice", "1990-01-01", "123")
    add_doctor(self.data["doctors"], "Dr. X", "Cardio")
    # Now both exist, can book
    book_appointment(self.data["appointments"], 1, 1, "2026-06-15 10:00",
                   self.data["patients"], self.data["doctors"])
```

Don't add entities in setUp unless ALL tests need them — it makes tests harder to reason about.
