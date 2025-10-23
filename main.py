import keyboard
import tkinter as tk
from tkinter import filedialog
import threading
import os
import json

# -----------------------------
# Global variables
mapping = {}
MAX_COMBO_LENGTH = 1
buffer = []
typed_stack = []
typing_enabled = True

# -----------------------------
# Load mapping from a JSON file
def load_mapping(filepath):
    global mapping, MAX_COMBO_LENGTH, buffer, typed_stack
    if not filepath or not os.path.exists(filepath):
        print("⚠️ Mapping file not found.")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        mapping = json.load(f)
    MAX_COMBO_LENGTH = max(len(k) for k in mapping)
    buffer.clear()
    typed_stack.clear()
    print(f"✅ Loaded mapping: {os.path.basename(filepath)}")

# -----------------------------
# Matching logic
def match_combo(buf):
    for length in range(min(len(buf), MAX_COMBO_LENGTH), 0, -1):
        seq = ''.join(buf[-length:])
        if seq in mapping:
            return seq, mapping[seq]["char"], length
    return None, None, 0

# -----------------------------
# Key handler
def on_key(e):
    global buffer, typed_stack, typing_enabled

    if e.event_type != "down":
        return

    if e.name == "esc":
        os._exit(0)

    if not typing_enabled:
        keyboard.send(e.name)
        return

    if e.name == "backspace":
        if typed_stack:
            back_len = typed_stack.pop()
            for _ in range(back_len):
                keyboard.send("backspace")
        else:
            keyboard.send("backspace")
        buffer.clear()
        return

    if e.name in ["space", "enter"]:
        keyboard.send(e.name)
        buffer.clear()
        typed_stack.clear()
        return

    if len(e.name) == 1:
        buffer.append(e.name)
        seq, tamil_char, match_len = match_combo(buffer)

        if match_len > 0:
            # Remove previously typed sequence if needed
            if match_len > 1 and typed_stack:
                erase_len = typed_stack.pop()
                for _ in range(erase_len):
                    keyboard.send("backspace")

            keyboard.write(tamil_char)
            typed_stack.append(len(tamil_char))
            buffer[:] = buffer[-MAX_COMBO_LENGTH:]
        else:
            keyboard.send(e.name)

# -----------------------------
# GUI loop
def gui_loop():
    global typing_enabled

    root = tk.Tk()
    root.title("5-Stage Tamil Keyboard")
    root.geometry("220x130+15+15")
    root.attributes("-topmost", True)
    root.resizable(False, False)

    def toggle_typing():
        global typing_enabled
        typing_enabled = not typing_enabled
        update_ui()

    def update_ui():
        if typing_enabled:
            label.config(text="🟢 Tamil ON", fg="green")
            toggle_btn.config(text="Turn OFF")
        else:
            label.config(text="🔴 Tamil OFF", fg="red")
            toggle_btn.config(text="Turn ON")

    def load_json():
        file = filedialog.askopenfilename(
            title="Select Tamil Phonetic JSON",
            filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
        )
        if file:
            load_mapping(file)

    def on_close():
        root.destroy()
        os._exit(0)

    # Widgets
    label = tk.Label(root, text="🟢 Tamil ON", font=("Arial", 14))
    label.pack(pady=5)

    toggle_btn = tk.Button(root, text="Turn OFF", font=("Arial", 12), command=toggle_typing)
    toggle_btn.pack(pady=2)

    load_btn = tk.Button(root, text="Load JSON", font=("Arial", 12), command=load_json)
    load_btn.pack(pady=5)

    update_ui()
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

# -----------------------------
# Main
if __name__ == "__main__":
    print("✅ 5-Stage Tamil Keyboard Running")
    print("🚪 Press ESC to quit")
    print("🔄 Use GUI to toggle Tamil/English or load new JSON")

    threading.Thread(target=gui_loop, daemon=True).start()
    keyboard.hook(on_key, suppress=True)
    keyboard.wait("esc")
