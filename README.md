# Keylogger Script

A Python-based keystroke monitoring tool designed to capture and log inputs locally for endpoint security auditing and system analysis.

---

## Features

* **Configurable Settings:** Manage log paths, filenames, and formatting through `config.json`.
* **Delimiter Flushing:** Buffers keystrokes and writes to disk only when specific delimiter keys are pressed.
* **Key Sanitization:** Automatically translates special keys (like `CTRL`, `SHIFT`, or `ENTER`) into clean, human-readable tags.
* **Synchronous Handling:** Captures input on key press events to maintain strict chronological order during rapid typing.

---

## Configuration (`config.json`)

Customize the tool by updating the parameters in `config.json`:

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `output_directory` | `string` | Save folder path. Leave as `""` to save in the script's directory. |
| `filename` | `string` | Name of the output log file (e.g., `keylog.txt`). |
| `flush_on_delimiter` | `boolean` | If `true`, writes logs only when a delimiter key is pressed. |
| `new_line_per_delimiter` | `boolean` | If `true`, starts a new line after every delimiter. |
| `stealth_mode` | `boolean` | *(Planned feature)* Toggles background execution mode. |

### Key Output Mapping

Special modifier keys are sanitized into explicit tags within the log file:

| Key | Log Output | Key | Log Output |
| :--- | :--- | :--- | :--- |
| **Enter** | `\n` *(Newline)* | **Shift** | ` [SHIFT] ` |
| **Space** | `" "` | **Ctrl** | ` [CTRL] ` |
| **Backspace** | ` [BACKSPACE] ` | **Alt** | ` [ALT] ` |
| **Tab** | ` [TAB] ` | **Delete** | ` [DELETE] ` |
| **Caps Lock** | ` [CAPS_LOCK] ` | **Escape** | ` [ESC] ` |

---

## Installation & Setup

### 1. Set Up Virtual Environment
From the repository root folder, run:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Tool
Navigate to the directory and launch the script:

```bash
cd monitoring/keylogger
python main.py
```

---

## Changelog

### [v1.1.0] - 2026-06-26
* **Added:** `config.json` support for dynamic settings management (paths, naming, delimiter flushing).
* **Improved:** Replaced inline string formatting with dictionary mapping.
* **Updated:** Cleaned up log tags for special control keys (`CTRL`, `ALT`, `SHIFT`, etc.).

### [v1.0.1] - 2026-06-11
* **Fixed:** Resolved character scrambling caused by asynchronous `on_release` event handling.
* **Changed:** Shifted key recording logic to synchronous `on_press` event handler.

### [v1.0.0] - 2026-06-07
* **Initial Release:** Implemented basic keylogging and sanitization (`ENTER`, `SPACE`, `BACKSPACE`).