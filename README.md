# Claude Camp W2 Exercises

Four Python practice projects from Week 2, covering **dictionaries · exception handling · file I/O**.

## Environment

- Python 3.8+
- No third-party dependencies

## Exercises

### 01 Student Roster Manager — [`01_roster.py`](./01_roster.py)
Manages student information (name, email, join date) using a dictionary. Command-line interface supporting add, query, and delete operations.

```bash
python 01_roster.py
```

### 02 Word Frequency Counter — [`02_word_count.py`](./02_word_count.py)
Takes text input and counts the frequency of each word. Output is sorted by frequency in descending order. Case-insensitive.

```bash
python 02_word_count.py
```

### 03 To-Do List — [`03_todo.py`](./03_todo.py)
Add, complete, and view tasks. Data is persisted to `todos.json` and automatically loaded on restart. Handles missing or corrupted files gracefully.

```bash
python 03_todo.py
```

### 04 Safe Calculator — [`04_calculator.py`](./04_calculator.py)
A four-function calculator (+, −, ×, ÷) with graceful handling of division by zero, non-numeric input, and `quit` to exit.

```bash
python 04_calculator.py
```

## Takeaways

- W1 was about *getting the workflow running*; W2 is about *building professional habits*
- One commit per exercise — building the muscle memory of "finish one, commit one"
- Exception handling = don't crash + give the user a friendly message