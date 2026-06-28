# Keylogger

A Python-based keystroke monitoring tool designed to capture and log inputs locally for endpoint security auditing and monitoring analysis.

## Features & Configuration
The script looks for a `config.json` file in the same directory. You can customize the following parameters:

* `output_directory`: The path where the log file will be saved. If left blank (`""`), it defaults to the directory where `main.py` is located.
* `filename`: The name of the generated log file.
* `flush_on_delimiter`: Buffers inputs and writes to the file only when a delimiter key is pressed.
* `new_line_per_delimiter`: Starts a fresh line in the log file after every delimiter.
* `stealth_mode`: *Planned feature (currently unavailable).*

### Key Sanitization Mapping
To ensure the log file remains clean and highly readable, special keys are dynamically captured and mapped to explicit text tags:

| Key | Log Output |
| :--- | :--- |
| `Enter` | `\n` (Actual Newline) |
| `Space` | `" "` (Spacebar) |
| `Backspace` | ` [BACKSPACE] ` |
| `Tab` | ` [TAB] ` |
| `Caps Lock` | ` [CAPS_LOCK] ` |
| `Shift (Left/Right)` | ` [SHIFT] ` |
| `Ctrl (Left/Right)` | ` [CTRL] ` |
| `Alt / AltGr` | ` [ALT] ` |
| `Delete` | ` [DELETE] ` |
| `Escape` | ` [ESC] ` |

---

## Installation & Usage

1. **Install dependencies:**
   ```bash
   pip install pynput
2. **Run the script:**
   ```bash
   python main.py
## Update Changelog
- 6/26/2026 — Configuration & Formatting Overhaul
  - 
    - Added `config.json` file support for dynamic settings management (paths, naming, delimiter flushing, and layout options).
    - Replaced inline string formatting checks with an optimized dictionary mapping layout.
    - Cleaned up log representations for special modifiers (`Ctrl`, `Alt`, `Shift`, `Tab`, `Caps Lock`, etc.) to keep logs looking uniform and organized.

- 6/11/2026 — Race Condition Fix
  - 
    - **Issue:** Characters and phrases occasionally became scrambled or printed out of sequence during rapid typing.
    - **Root Cause:** Input logs were bound to the asynchronous `on_release` listener event. Rapid typing overlapping caused thread blocks to record actions out of order.
    - **Resolution:** Migrated character tracking entirely to the synchronous `on_press` event handler; deprecated `on_release`logic.

- 6/07/2026 — Basic Key Sanitization
  - 
    - Initial implementation of raw string scrubbing for basic keys (Enter, Backspace, Space) to improve general analytical output in keylog.txt.
