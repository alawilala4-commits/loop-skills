# Playlist CLI App Usage

This note covers the typical usage pattern for the `playlist.py` CLI app (a music playlist manager).

## Commands

- **Add a song**
  ```bash
  python playlist.py add "Judul Lagu" "Nama Artis" --album "Nama Album" --genre "Pop" --duration "3:45"
  ```
  Optional flags: `--album`, `--genre`, `--duration` (format MM:SS or H:MM:SS).

- **List all songs**
  ```bash
  python playlist.py list
  ```

- **Search by keyword** (searches title, artist, album, genre)
  ```bash
  python playlist.py search "Judol"
  ```

- **Remove a song by ID**
  ```bash
  python playlist.py remove 3
  ```

- **View details of a song**
  ```bash
  python playlist.py view 3
  ```

- **Statistics**
  ```bash
  python playlist.py stats
  ```

- **Clear all songs**
  ```bash
  python playlist.py clear
  ```

## Persistence

Data is stored automatically in `playlist.json` located in the same directory as `playlist.py`. The file is created on first run and updated after each modifying command.

## Testing Tips

When writing tests for `playlist.py`, consider mocking:

- `input()` for interactive prompts (if any).
- `json.load`/`json.dump` to avoid touching the real file during unit tests.
- `os.path.exists` to simulate first-run vs existing file.

Example test for add command:

```python
@patch('builtins.input', side_effect=['Judol', 'Artis'])
def test_add_song(mock_input):
    from playlist import add_song
    songs = []
    songs = add_song(songs, 'Judol', 'Artis')
    assert len(songs) == 1
    assert songs[0]['title'] == 'Judol'
```

## Common Pitfalls

- Forgetting to call `save_playlist()` after modifying the in‑place list.
- Using mutable default arguments in helper functions.
- Not validating duration format before storing.