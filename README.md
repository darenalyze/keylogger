# Keylogger Script

A Python-based keystroke monitoring tool designed to capture and log inputs locally for endpoint security auditing and system analysis.

---

## Features

* **Configurable Settings:** Manage log paths, filenames, formatting, and key maps through `config.json`.
* **Delimiter Flushing:** Buffers keystrokes and writes to disk only when specific flush keys are pressed.
* **Key Sanitization:** Automatically translates special keys (like `CTRL`, `SHIFT`, or `ENTER`) into clean, human-readable tags.
* **Synchronous Handling:** Captures input on key press events to maintain strict chronological order during rapid typing.

---

## Configuration (`config.json`)

Customize the tool by updating the parameters in `config.json`. The settings are grouped into three main categories:

### 1. Logging Settings (`logging`)
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `output_directory` | `string` | Save folder path. Leave as `null` to save in the script's directory. |
| `filename` | `string` | Name of the output log file (e.g., `keylog.txt`). |

### 2. Format Settings (`format`)
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `flush_only_on_flush_keys` | `boolean` | If `true`, writes logs to the file only when a flush key is pressed. |
| `newline_on_specific_keys_only` | `boolean` | If `true`, starts a new line only when a specified newline key is pressed. |
| `newline_after_every_key` | `boolean` | If `true`, starts a new line after every single keystroke. |
| `timestamp_per_line` | `boolean` | If `true`, adds the date and time at the start of each new line. |

### 3. Key Settings (`keys`)
You can now define trigger keys and mapping outputs directly in the config file:
* **`newline_keys`**: List of keys that trigger a new line in the log.
* **`flush_keys`**: List of keys that trigger saving the buffer to the file.
* **`key_map`**: Custom text tags for special keys (e.g., mapping `enter` to `[ENTER]`).

---

## Installation & Setup
### Requirements:
- python3-venv
- python3

If the above is not installed yet, run this command:

#### Linux:
**1. Installing required packages and Extension**
```bash
sudo apt update
sudo apt install python3 python3-venv -y
```

**2. Set Up Virtual Environment**
From the repository root folder, run:
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the Tool**
Navigate to the directory and launch the script:
```bash
cd monitoring/keylogger
python main.py
```

#### Windows:
(Run the cmd as administrator)  
**1. Installing required application:**
```cmd
winget install python
```

**2. Creating venv**
```cmd
cd keylogger
python -m venv venv
```

**3. Activating the venv**
```cmd
venv\Scripts\activate ```

**4. Installing dependencies**
```cmd
python -m pip install -r requirements.txt
```

**5. Run the tool**
```cmd
python main.py
```

---

## Changelog

### [v1.2.0] - 2026-10-04
- **Added:** Moved `newline_keys`, `flush_keys`, and `key_map` into `config.json` for easy editing without touching the code.
- **Changed:** Grouped configuration variables into `logging`, `format`, and `keys` sections. 
- **Changed:** Renamed format settings to use clear, readable names.
- **Removed:** Deleted the `date_and_time_per_key` feature.
- **Fixed:** Spacebar is now correctly recorded as a blank space in the log instead of being skipped.

### [v1.1.1] - 2026-10-02  
- **Improve:** Code readability and improve `config.json` file simplicity.

### [v1.1.0] - 2026-06-26
- **Added:** `config.json` support for dynamic settings management (paths, naming, delimiter flushing).
- **Improved:** Replaced inline string formatting with dictionary mapping.
- **Updated:** Cleaned up log tags for special control keys (`CTRL`, `ALT`, `SHIFT`, etc.).

### [v1.0.1] - 2026-06-11
- **Fixed:** Resolved character scrambling caused by asynchronous `on_release` event handling.
- **Changed:** Shifted key recording logic to synchronous `on_press` event handler.

### [v1.0.0] - 2026-06-07
- **Initial Release:** Implemented basic keylogging and sanitization (`ENTER`, `SPACE`, `BACKSPACE`).
