# Module & Packager — Multi-Utility Toolkit

A beginner-friendly **menu-driven Python project** showing how standard modules, reusable custom modules, packages, `match-case`, `__name__ == "__main__"`, and `dir()` work together.

## Requirements

- **Python 3.10 or newer** (for `match-case`).
- **No third-party packages** or API keys.

## Project structure

```text
Module-and-Packager-FINAL/
├── main.py                  # All menus and the main program
├── toolkit/
│   ├── __init__.py          # Initializes the custom package
│   ├── file_utils.py        # Create, write, read, append text files
│   └── math_utils.py        # Kilometer / temperature conversions
├── README.md                # Project guide
└── SAMPLE_OUTPUT.txt        # Example console results
```

The program creates **`toolkit_log.txt`** after your first logged operation. Your own practice text files are created only when you use the File Operations menu.

## How to run

1. Extract the ZIP and open a terminal **inside the project folder**.
2. Run `python main.py` (on some computers, use `python3 main.py`).
3. Select a main-menu option (`1` to `7`), then a submenu option. All submenus have a Back option. Main-menu option `7` exits.

## All project features

| Main menu | Operations |
| --- | --- |
| **1. Datetime and Time** | Display current date and time; difference between dates or times; `strftime()` date formatting; stopwatch; countdown timer; calculate working hours (including overnight shifts). |
| **2. Mathematics** | Arithmetic (+ − × ÷); factorial; compound interest; sin/cos/tan; logarithm; circle/rectangle/triangle areas (geometry); custom kilometer-to-mile and Celsius-to-Fahrenheit conversions. |
| **3. Random** | Generate random number, random list, password, OTP; sample items from a dataset; play a dice-guessing game. |
| **4. UUID** | Make `uuid.uuid4()` identifiers for files, records/invoices, and sessions. |
| **5. File Operations** | Create, write (replace), read, and append (update) text files using `toolkit.file_utils`. |
| **6. `dir()` Exploration** | Dynamically import and list attributes for **any importable built-in or custom module**, e.g. `math`, `time`, `uuid`, `toolkit.math_utils`, or `toolkit.file_utils`. |
| **7. Exit** | Stop the program cleanly. |

## Notes for beginners

- Dates must be entered in `YYYY-MM-DD` format; times use 24-hour `HH:MM` format.
- For clock-time differences and working hours, if the end time is earlier than the start time, the program considers the end to be **the next day**. Identical times count as 0 hours, not a full day.
- Compound interest displays **both the final amount and the interest earned** (the principal is part of the final amount).
- The trigonometry menu takes **degrees**, converts them with `math.radians`, and displays tangent as `undefined` near angles like 90°.
- For dataset sampling, enter comma-separated items. A sample cannot be larger than the input list.
- For the dice game, guess 1 through 6 and see whether your guess matches the random dice roll.
- `toolkit.math_utils` contains reusable calculation functions. `toolkit.file_utils` contains file-writing functions used both by the File Operations menu and the output log.
- `__init__.py` makes `toolkit` a package. The `if __name__ == "__main__":` guard in `main.py` makes sure the interactive menu runs only when executed directly.
- The module explorer uses Python's `__import__()` and `dir()`; only choose modules you trust. It works with importable standard modules and custom modules available on the Python import path.
- **Log file:** operation results, errors, generated UUIDs, timer output, and text-file reads are logged to `toolkit_log.txt` through `file_utils.append_file`. Menu headings and input prompts are not logged. **Password and OTP values are not logged** for privacy; only a message that one was generated is recorded.
- **File safety:** Create New File refuses to overwrite an existing file. Write / Replace File Content intentionally replaces existing contents; use a practice `.txt` file. `toolkit_log.txt` is reserved in the menu to avoid accidental changes.
- Invalid numeric inputs and file errors are handled in the menu so you can try again.

## Real-world practice example

A small business can use this toolkit to calculate overnight working hours, generate a temporary password, assign a UUID to an invoice, write notes to a text file, and inspect modules with `dir()`.

See `SAMPLE_OUTPUT.txt` for example runs. The clock, UUIDs, random values, and elapsed times will differ on each run.
