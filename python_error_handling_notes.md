# Python Error Handling — Complete Notes

---

## 1. Errors vs Exceptions

Python has two broad categories of problems:

| Type | When it happens | Example |
|---|---|---|
| **Syntax Error** | Before the code even runs — Python can't parse it | `if x = 5:` (missing `==`) |
| **Exception** | While the code is running (runtime) | `10 / 0`, `int("abc")` |

```python
# Syntax Error — code won't even start
if x = 5:        # SyntaxError: invalid syntax
    print(x)

# Exception — code runs, then breaks at this line
x = 10 / 0        # ZeroDivisionError: division by zero
```

Error handling (`try`/`except`) deals with **exceptions**, not syntax errors — syntax errors must be fixed before the program runs at all.

---

## 2. The Basic try-except Block

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number!")
```

- Code that *might* fail goes in `try`.
- If an exception occurs, Python jumps straight to the matching `except` block — remaining `try` lines are skipped.
- If no exception occurs, all `except` blocks are skipped entirely.

---

## 3. Catching Specific vs Multiple Exceptions

**Always catch the most specific exception you can.** Avoid a bare `except:` — it hides bugs (even catches `KeyboardInterrupt`, typos in variable names, etc.).

```python
# Bad — swallows everything, including your own bugs
try:
    file = open("missing.csv")
except:
    print("Something went wrong")
# Output: Something went wrong   (you have NO idea why it failed)

# Good — specific and predictable
try:
    file = open("missing.csv")
except FileNotFoundError:
    print("File missing")
except PermissionError:
    print("No permission to access file")
# Output: File missing   (you know EXACTLY what happened)
```

**Catching multiple exceptions in one block** (use a tuple):

```python
try:
    data = [1, 2, 3]
    print(data[5])
except (IndexError, KeyError) as e:
    print(f"Lookup failed: {e}")
```

---

## 4. Accessing the Exception Object

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(e)              # division by zero
    print(type(e))        # <class 'ZeroDivisionError'>
    print(e.args)         # ('division by zero',)
```

`as e` binds the exception instance so you can inspect its message, type, or arguments — useful for logging.

---

## 5. else and finally

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division failed")
else:
    # Runs ONLY if no exception was raised in try
    print(f"Success: {result}")
finally:
    # Runs ALWAYS — exception or not, even if there's a return/break
    print("Cleanup done")
```

| Clause | Runs when |
|---|---|
| `except` | An exception matching it was raised |
| `else` | No exception was raised in `try` |
| `finally` | Always — used for cleanup (closing files, DB connections, releasing locks) |

**Real-world pattern** (why `finally` matters):

```python
file = None
try:
    file = open("data.csv", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()   # guaranteed to run, preventing resource leaks
```

---

## 6. Raising Exceptions Yourself — `raise`

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

set_age(-5)   # ValueError: Age cannot be negative
```

**Re-raising** an exception after partial handling (e.g., logging it, then letting it propagate):

```python
def process_data(value):
    if value < 0:
        raise ValueError(f"value must be non-negative, got {value}")
    return value * 2

try:
    process_data(-5)
except ValueError as e:
    print(f"Logging error: {e}")   # Logging error: value must be non-negative, got -5
    raise                          # re-raises the SAME exception, with original traceback
```

**Exception chaining** with `raise ... from` — preserves the original cause when converting one exception into another:

```python
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Failed to parse config") from e
```

---

## 7. Custom (User-Defined) Exceptions

Create your own exception classes by inheriting from `Exception` (or a more specific built-in). This makes error handling in larger projects far more readable.

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}; balance is only {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(1000, 5000)
except InsufficientFundsError as e:
    print(e)                 # Cannot withdraw 5000; balance is only 1000
    print(e.balance, e.amount)  # 1000 5000
```

**Why custom exceptions?**
- Callers can catch `InsufficientFundsError` specifically instead of a generic `Exception`.
- You can attach extra data to the exception (like `balance`, `amount` above).
- Makes large codebases self-documenting.

---

## 8. The Built-in Exception Hierarchy

All exceptions inherit from `BaseException`. The ones you'll actually use inherit from `Exception`.

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      ├── AttributeError
      ├── FileNotFoundError (subclass of OSError)
      ├── ImportError
      ├── StopIteration
      └── RuntimeError
```

| Exception | Common trigger |
|---|---|
| `ValueError` | Right type, wrong value — `int("abc")` |
| `TypeError` | Wrong type — `"2" + 2` |
| `KeyError` | Missing dict key — `d["missing"]` |
| `IndexError` | List index out of range — `[1,2][5]` |
| `AttributeError` | Attribute/method doesn't exist — `None.append(1)` |
| `FileNotFoundError` | File path doesn't exist |
| `ZeroDivisionError` | Dividing by zero |
| `ImportError` / `ModuleNotFoundError` | Missing or bad import |
| `StopIteration` | Iterator exhausted (raised internally by `next()`) |

> **Never catch `BaseException`** directly — it includes `SystemExit` and `KeyboardInterrupt`, so you'd block `Ctrl+C` and clean program exits.

---

## 9. `assert` — Debugging, Not Error Handling

```python
def get_average(scores):
    assert len(scores) > 0, "scores list cannot be empty"
    return sum(scores) / len(scores)
```

- Raises `AssertionError` if the condition is `False`.
- **Not for production input validation** — assertions are stripped out when Python runs with the `-O` (optimize) flag. Use `raise ValueError(...)` for real validation; use `assert` for catching your own logic bugs during development/testing.

---

## 10. EAFP vs LBYL

Two philosophies for handling risky operations:

```python
# LBYL — "Look Before You Leap" (check first, act second)
if "key" in my_dict:
    value = my_dict["key"]
else:
    value = None

# EAFP — "Easier to Ask Forgiveness than Permission" (try first, handle failure)
try:
    value = my_dict["key"]
except KeyError:
    value = None
```

Python's culture favors **EAFP** — it's often faster (no double lookup) and avoids race conditions (e.g., a file existing at check-time but not at open-time).

---

## 11. Context Managers (`with`) — Cleaner Alternative to try/finally

```python
# Manual (error-prone if you forget close())
f = open("data.csv")
try:
    data = f.read()
finally:
    f.close()

# With a context manager — cleanup is automatic and guaranteed
with open("data.csv") as f:
    data = f.read()
# file is closed here automatically, even if an exception occurred
```

Common uses: file handling, database connections, `threading.Lock()`, `pandas`/`requests` sessions.

---

## 12. Logging Exceptions Properly

In real projects, prefer `logging` over bare `print()` for exceptions:

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Division failed")   # logs message + full traceback automatically
```

`logging.exception()` (called inside an `except` block) automatically includes the traceback — invaluable for debugging in production.

---

## 13. Putting It All Together — Full Example

```python
import logging

logging.basicConfig(level=logging.INFO)

class InvalidRecordError(Exception):
    """Raised when a data record fails validation."""
    pass

def parse_record(record):
    if "id" not in record:
        raise InvalidRecordError(f"Missing 'id' field: {record}")
    if not isinstance(record["value"], (int, float)):
        raise InvalidRecordError(f"'value' must be numeric: {record}")
    return record["value"]

def process_records(records):
    total = 0
    errors = 0
    for record in records:
        try:
            total += parse_record(record)
        except InvalidRecordError as e:
            logging.error(f"Skipping bad record: {e}")
            errors += 1
        except Exception as e:
            # Catch-all for anything truly unexpected, logged with traceback
            logging.exception("Unexpected error while processing record")
            errors += 1
        else:
            logging.info(f"Record processed successfully: {record}")
        finally:
            pass  # placeholder for per-record cleanup if needed
    return total, errors

records = [
    {"id": 1, "value": 100},
    {"id": 2, "value": "bad"},
    {"value": 50},
]

total, errors = process_records(records)
print(f"Total: {total}, Errors: {errors}")
```

---

## 14. Common Interview Questions

**Q: What's the difference between `Exception` and `BaseException`?**
`BaseException` is the root of all exceptions, including `SystemExit` and `KeyboardInterrupt`. `Exception` is the subclass you should actually catch/inherit from — catching `BaseException` risks swallowing program-exit signals.

**Q: Difference between `except Exception as e` and a bare `except:`?**
A bare `except:` catches everything, including `BaseException` subclasses like `KeyboardInterrupt`. `except Exception as e` is scoped to normal errors and gives you access to the exception object.

**Q: What happens if an exception occurs inside a `finally` block?**
It propagates normally and can even suppress an exception that was already in flight from `try`/`except` — this is a common gotcha, so keep `finally` blocks simple.

**Q: Can you have multiple `except` blocks for one `try`?**
Yes — Python checks them top to bottom and runs the first match. Order matters: put more specific exceptions before more general ones (e.g., `ValueError` before `Exception`), since a broader one placed first will shadow the rest.

**Q: What's the difference between `raise` and `raise Exception("msg") from e`?**
Plain `raise` (with no argument) inside an `except` re-raises the currently-handled exception unchanged. `raise NewException(...) from e` raises a *new* exception while explicitly recording `e` as its cause (shown in the traceback as "The above exception was the direct cause of...").

**Q: Why avoid using exceptions for normal control flow?**
Exceptions are for *exceptional* cases. Overusing them for routine logic (e.g., using `StopIteration` manually instead of a loop condition) hurts readability and performance versus straightforward conditionals — though EAFP-style `try/except` for expected edge cases (like a missing dict key) is still considered good Python style.

---

## 15. Quick Reference / Cheat Sheet

```python
try:
    result = 10 / int(user_input)          # might raise ValueError or ZeroDivisionError
except ValueError as e:
    print(f"Invalid input: {e}")
except (ZeroDivisionError, TypeError) as e:
    print(f"Calculation error: {e}")
else:
    print(f"Result: {result}")             # only runs if try succeeded
finally:
    print("Done")                          # always runs

raise ValueError("Age cannot be negative")            # raise your own
raise                                                  # re-raise current exception
raise RuntimeError("Failed to load config") from e     # chain exceptions

class InsufficientFundsError(Exception):
    pass

assert age >= 0, "age must be non-negative"            # debugging only, not validation

with open("data.csv") as f:                            # preferred over manual try/finally
    data = f.read()
```

**Best practices checklist:**
- Catch specific exceptions, never bare `except:`
- Put specific `except` blocks before general ones
- Use `finally` (or better, `with`) for guaranteed cleanup
- Use `logging.exception()` in production, not `print()`
- Reserve `assert` for internal invariants/debugging, not input validation
- Write custom exceptions for domain-specific errors in larger projects
- Prefer EAFP (`try`/`except`) over excessive pre-checking (LBYL) in idiomatic Python
