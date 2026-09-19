# Python File Handling — Complete Notes

---

## 1. What Is File Handling?

File handling means reading data from, and writing data to, files on disk — text files, CSVs, JSON, logs, binary files, etc. Python does this through **file objects**, created with the built-in `open()` function.

```python
f = open("data.txt", "r")   # opens a file object
content = f.read()
f.close()                    # must close manually if opened this way
```

---

## 2. File Modes

The second argument to `open()` controls how the file is accessed:

| Mode | Meaning | Creates file if missing? | Overwrites existing content? |
|---|---|---|---|
| `"r"` | Read (default) | No — raises `FileNotFoundError` | No |
| `"w"` | Write | Yes | **Yes** — truncates to empty |
| `"a"` | Append | Yes | No — writes go to the end |
| `"x"` | Exclusive create | Yes | Raises `FileExistsError` if it already exists |
| `"r+"` | Read + Write | No | No — overwrites only where you write |
| `"w+"` | Write + Read | Yes | **Yes** |
| `"a+"` | Append + Read | Yes | No |
| `"b"` suffix (e.g. `"rb"`, `"wb"`) | Binary mode | — | — |
| `"t"` suffix (e.g. `"rt"`) | Text mode (default) | — | — |

```python
open("f.txt", "r")    # read text
open("f.txt", "w")    # write text (overwrites!)
open("f.txt", "a")    # append text
open("img.png", "rb") # read binary (images, PDFs, etc.)
```

> **Common gotcha:** `"w"` mode **erases the file's existing content the moment you open it** — even if you never call `.write()`. Use `"a"` if you want to keep existing content.

---

## 3. Reading Files

```python
with open("data.txt", "r") as f:
    content = f.read()          # entire file as ONE string
```

```python
with open("data.txt", "r") as f:
    line = f.readline()         # reads just ONE line (including \n)
```

```python
with open("data.txt", "r") as f:
    lines = f.readlines()       # list of all lines, e.g. ['line1\n', 'line2\n']
```

**Most memory-efficient way — iterate line by line** (doesn't load the whole file into memory, important for large files):

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())     # .strip() removes the trailing \n
```

---

## 4. Writing and Appending

```python
# write() — overwrites the file entirely
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")

# writelines() — writes a list of strings (does NOT add \n automatically)
with open("output.txt", "w") as f:
    lines = ["First\n", "Second\n", "Third\n"]
    f.writelines(lines)

# append — adds to the end without erasing existing content
with open("output.txt", "a") as f:
    f.write("Appended line\n")
```

---

## 5. Why `with` Instead of Manual `open()`/`close()`

```python
# Manual — risky: if an exception happens before close(), the file stays open
f = open("data.txt", "r")
data = f.read()
f.close()

# Safer manual version
f = open("data.txt", "r")
try:
    data = f.read()
finally:
    f.close()

# Best — the 'with' statement (context manager) closes automatically,
# even if an exception is raised inside the block
with open("data.txt", "r") as f:
    data = f.read()
# f is already closed here — guaranteed
```

`with` is the **standard, idiomatic** way to handle files in Python — always prefer it. It relies on the file object being a **context manager**, which handles cleanup via `__enter__`/`__exit__` behind the scenes.

**Reading/writing multiple files at once:**

```python
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
```

---

## 6. File Object Attributes & Methods

```python
with open("data.txt", "r") as f:
    print(f.name)      # data.txt
    print(f.mode)       # r
    print(f.closed)     # False (True after the 'with' block ends)

    print(f.tell())     # current cursor position (byte offset), starts at 0
    f.seek(5)           # move cursor to byte 5
    print(f.tell())     # 5
```

`seek()` and `tell()` matter when you need to re-read a section of a file or track your position without reopening it.

---

## 7. Handling File-Related Exceptions

Ties directly into general error handling — file operations are one of the most common sources of runtime exceptions:

```python
try:
    with open("missing.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("No permission to read this file")
except IsADirectoryError:
    print("That's a directory, not a file")
```

| Exception | When it happens |
|---|---|
| `FileNotFoundError` | Opening a file in `"r"` mode that doesn't exist |
| `PermissionError` | No OS-level permission to read/write the file |
| `IsADirectoryError` | Path points to a directory, not a file |
| `FileExistsError` | Using `"x"` mode on a file that already exists |
| `UnicodeDecodeError` | Reading text with the wrong encoding |

**Encoding gotcha** — always be explicit for text files, especially on Windows:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

---

## 8. Checking Paths — `os.path` and `pathlib`

```python
import os

os.path.exists("data.txt")        # True/False
os.path.isfile("data.txt")        # True if it's a file
os.path.isdir("my_folder")        # True if it's a directory
os.path.getsize("data.txt")       # size in bytes
os.path.join("folder", "file.txt")  # OS-safe path joining
```

**Modern alternative — `pathlib` (preferred in new code):**

```python
from pathlib import Path

p = Path("data.txt")
p.exists()          # True/False
p.is_file()          # True/False
p.suffix             # '.txt'
p.stem               # 'data'
p.parent             # folder containing it

# pathlib also opens files directly
content = p.read_text(encoding="utf-8")
p.write_text("new content", encoding="utf-8")
```

---

## 9. Working with Directories

```python
import os

os.listdir(".")            # list files/folders in current directory
os.mkdir("new_folder")     # create one folder
os.makedirs("a/b/c")       # create nested folders
os.remove("file.txt")      # delete a file
os.rmdir("empty_folder")   # delete an EMPTY folder

import shutil
shutil.rmtree("folder")    # delete a folder AND its contents
shutil.copy("src.txt", "dst.txt")   # copy a file
```

---

## 10. CSV Files (`csv` module)

Directly relevant for data work — reading/writing tabular data without pandas.

```python
import csv

# Reading
with open("data.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)          # skip header row
    for row in reader:
        print(row)                 # row is a list, e.g. ['1', 'Alice', '85']

# Reading as dictionaries (column name -> value)
with open("data.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["score"])

# Writing
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "score"])
    writer.writerows([[1, "Alice", 85], [2, "Bob", 90]])
```

> `newline=""` when opening CSVs is important on Windows — without it, `csv` can insert extra blank rows.

---

## 11. JSON Files (`json` module)

```python
import json

# Reading JSON from a file into a Python dict/list
with open("config.json", "r") as f:
    data = json.load(f)
print(data["name"])

# Writing a Python object to a JSON file
data = {"name": "Alice", "scores": [85, 90, 78]}
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

# Converting to/from JSON strings (not files) — json.loads / json.dumps
json_string = json.dumps(data)      # dict -> string
parsed = json.loads(json_string)    # string -> dict
```

`load`/`dump` work with **file objects**; `loads`/`dumps` work with **strings** — a very common interview mix-up.

---

## 12. Binary Files

```python
# Copying an image byte-for-byte
with open("photo.jpg", "rb") as src, open("copy.jpg", "wb") as dst:
    dst.write(src.read())
```

Use `"b"` mode whenever the file isn't plain text (images, PDFs, executables, pickled Python objects) — opening binary data in text mode corrupts it via encoding/decoding.

---

## 13. Reading Large Files in Chunks

`read()` and `readlines()` load the **entire** file into memory — fine for small files, but a problem once a file is bigger than your available RAM. For plain-text files, line-by-line iteration (Section 3) already solves this. For files with no line structure (or very long lines), read fixed-size chunks instead:

```python
def read_in_chunks(filepath, chunk_size=1024 * 1024):  # 1 MB at a time
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

for chunk in read_in_chunks("huge_log.txt"):
    process(chunk)   # handle one chunk at a time, never the whole file
```

Using a generator (`yield`) means only one chunk is ever in memory at a time, no matter how large the file is.

---

## 14. pandas File I/O — Data Analyst Essentials

In real data-analyst work, file I/O usually goes through **pandas**, not the raw `csv`/`json` modules. Interviewers for this kind of role often check both layers — `csv`/`json` show you understand what's happening underneath, `pandas` is what you'll actually use day to day.

```python
import pandas as pd

# CSV
df = pd.read_csv("data.csv")             # straight into a DataFrame
df.to_csv("output.csv", index=False)     # index=False avoids writing row numbers as a column

# Excel
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
df.to_excel("output.xlsx", index=False)

# JSON
df = pd.read_json("data.json")
df.to_json("output.json", orient="records")

# A huge CSV that won't fit in memory — process it in chunks
for chunk in pd.read_csv("huge_file.csv", chunksize=100_000):
    process(chunk)     # each chunk is a DataFrame of 100,000 rows
```

| Raw Python | pandas equivalent |
|---|---|
| `csv.reader` / `csv.DictReader` | `pd.read_csv()` |
| `csv.writer` | `df.to_csv()` |
| `json.load()` | `pd.read_json()` |
| manual chunked reading | `chunksize=` parameter |

---

## 15. Writing Your Own Context Manager

`with` works because the object implements `__enter__` and `__exit__` — a common "explain how `with` actually works" interview question.

```python
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return False   # False = don't suppress exceptions raised inside the block

with ManagedFile("data.txt", "w") as f:
    f.write("Hello!")
```

**Simpler way, using `contextlib`:**

```python
from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with managed_file("data.txt", "w") as f:
    f.write("Hello!")
```

---

## 16. Complete Example — Putting It All Together

```python
import csv
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

def load_scores(filepath):
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"{filepath} does not exist")

    scores = []
    try:
        with open(path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    scores.append(float(row["score"]))
                except (ValueError, KeyError) as e:
                    logging.warning(f"Skipping bad row {row}: {e}")
    except PermissionError:
        logging.error(f"No permission to read {filepath}")
        raise

    return scores

def save_summary(scores, output_path):
    avg = sum(scores) / len(scores) if scores else 0
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Count: {len(scores)}\n")
        f.write(f"Average: {avg:.2f}\n")

scores = load_scores("students.csv")
save_summary(scores, "summary.txt")
print("Done — see summary.txt")
```

---

## 17. Common Interview Questions

**Q: What's the difference between `read()`, `readline()`, and `readlines()`?**
`read()` returns the whole file as one string. `readline()` returns just the next single line. `readlines()` returns a list of every line. For large files, iterating the file object directly (`for line in f:`) is preferred over `readlines()` since it doesn't load everything into memory at once.

**Q: Why is `with open(...) as f` preferred over manual `open()`/`close()`?**
`with` guarantees the file is closed even if an exception occurs inside the block — manual `close()` calls get skipped if an error happens first, unless wrapped in `try`/`finally`.

**Q: What happens if you open a file in `"w"` mode that already has content?**
The existing content is erased immediately when the file is opened — before you even call `.write()`. Use `"a"` (append) to preserve it.

**Q: Difference between `json.load()`/`json.dump()` and `json.loads()`/`json.dumps()`?**
The `load`/`dump` pair works directly with file objects; the `loads`/`dumps` pair (note the trailing "s" for "string") works with in-memory strings.

**Q: How do you read a very large file without running out of memory?**
Iterate over the file object line by line (`for line in f:`) rather than calling `.read()` or `.readlines()`, which load the entire file into memory at once.

**Q: What does `seek(0)` do?**
Moves the file's internal cursor back to the beginning (byte offset 0), so the next `read()` starts from the start of the file again — useful when you've already read a file and need to re-read it without reopening.

**Q: How does the `with` statement actually work?**
The object it's given must implement `__enter__` and `__exit__`. Python calls `__enter__()` on entry (its return value is bound to the `as` variable) and guarantees `__exit__()` runs on the way out — exception or not — which is how cleanup happens automatically. Any object with both methods is called a context manager; you can write your own as a class, or more simply with `@contextlib.contextmanager`.

**Q: How would you process a file too large to fit in memory?**
Never call `.read()` or `.readlines()` on it. Instead iterate line by line (`for line in f:`), or read fixed-size chunks with `f.read(chunk_size)` in a loop, or — in a pandas context — pass `chunksize=` to `pd.read_csv()` and process one chunk (DataFrame) at a time.

**Q: What's the difference between the `csv`/`json` modules and pandas' `read_csv`/`read_json`?**
`csv`/`json` are lower-level — they read into plain Python lists/dicts and give you full control row by row. `pandas` reads directly into a DataFrame, is far faster for large tabular data, and includes built-in handling for chunking, dtypes, and missing values — it's the tool you'd actually reach for in day-to-day data-analyst work.

---

## 18. Quick Reference / Cheat Sheet

```python
# Opening
with open("file.txt", "r", encoding="utf-8") as f:
    ...

# Reading
f.read()          # whole file as a string
f.readline()      # one line
f.readlines()     # list of all lines
for line in f:    # memory-efficient, line by line
    ...

# Writing
f.write("text")         # write a string
f.writelines(list_of_str)  # write multiple strings (no auto \n)

# Modes
"r"  read (default)      "w"  write (overwrites)   "a"  append
"x"  create (error if exists)   "b" suffix = binary   "+" suffix = read+write

# Paths
from pathlib import Path
Path("f.txt").exists()
Path("f.txt").read_text()
Path("f.txt").write_text("data")

# CSV
import csv
csv.reader(f) / csv.writer(f)
csv.DictReader(f) / csv.DictWriter(f)

# JSON
import json
json.load(f)   / json.dump(data, f)     # file <-> object
json.loads(s)  / json.dumps(data)       # string <-> object

# Common exceptions
FileNotFoundError, PermissionError, IsADirectoryError, FileExistsError

# Large files
for chunk in pd.read_csv("big.csv", chunksize=100_000):
    ...
while chunk := f.read(1024 * 1024):
    ...

# Custom context manager
from contextlib import contextmanager

@contextmanager
def managed_file(name, mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()
```

**Best practices checklist:**
- Always use `with open(...)` — never rely on manual `close()`
- Specify `encoding="utf-8"` explicitly for text files
- Use `"a"` instead of `"w"` when you don't want to erase existing content
- Iterate line-by-line (or in chunks) for large files instead of `read()`/`readlines()`
- Use `newline=""` when opening files for the `csv` module
- Wrap file operations in `try`/`except` for `FileNotFoundError`/`PermissionError`
- Prefer `pathlib` over `os.path` in new code — more readable, object-oriented API
- For tabular data, prefer `pandas` (`read_csv`/`read_excel`) over manual `csv` parsing unless you need low-level row control
