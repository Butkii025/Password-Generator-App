import tkinter as tk
import secrets
import string

def generate_password():
    # 1. Gather choices from checkboxes
    pool = ""
    if use_upper.get():
        pool += string.ascii_uppercase
    if use_lower.get():
        pool += string.ascii_lowercase
    if use_digits.get():
        pool += string.digits
    if use_symbols.get():
        pool += string.punctuation

    # 2. Validation: If no checkboxes are selected, warn the user
    if not pool:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "⚠️ Select at least one option!")
        return

    # 3. Securely generate the password based on slider length
    length = length_slider.get()
    # secrets.choice is cryptographically secure compared to standard random.choice
    password = "".join(secrets.choice(pool) for _ in range(length))

    # 4. Display the generated password in the app
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    status_label.config(text="") # Clear any previous status message

def copy_to_clipboard():
    password = password_entry.get()
    # Check if there is a valid password to copy
    if password and "⚠️" not in password and password != "Copied! ✅":
        root.clipboard_clear()
        root.clipboard_append(password)
        status_label.config(text="Copied to clipboard! ✅", fg="#4caf50")
    else:
        status_label.config(text="Nothing valid to copy!", fg="#e91e63")

# --- UI Setup ---
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("450x450")
root.configure(bg="#1a1a2e") # Deep dark aesthetic

# Title
title_lbl = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#1a1a2e", fg="#e2e2e2")
title_lbl.pack(pady=15)

# Password Display Field Box
password_entry = tk.Entry(root, font=("Courier", 14), width=30, justify="center", bd=0, bg="#16213e", fg="#00f5d4")
password_entry.pack(pady=10, ipady=5)

# Length Slider
slider_frame = tk.Frame(root, bg="#1a1a2e")
slider_frame.pack(pady=10)
tk.Label(slider_frame, text="Length:", font=("Arial", 11), bg="#1a1a2e", fg="#e2e2e2").grid(row=0, column=0, padx=5)

length_slider = tk.Scale(slider_frame, from_=8, to=32, orient="horizontal", length=200, bg="#1a1a2e", fg="#e2e2e2", highlightthickness=0, troughcolor="#16213e", activebackground="#00f5d4")
length_slider.set(14) # Default secure length
length_slider.grid(row=0, column=1)

# Checkbox Variables
use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

# Checkbox UI Layout Container
cb_frame = tk.Frame(root, bg="#1a1a2e")
cb_frame.pack(pady=15)

tk.Checkbutton(cb_frame, text="Uppercase (A-Z)", variable=use_upper, bg="#1a1a2e", fg="#e2e2e2", selectcolor="#16213e", activebackground="#1a1a2e", activeforeground="#e2e2e2").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Checkbutton(cb_frame, text="Lowercase (a-z)", variable=use_lower, bg="#1a1a2e", fg="#e2e2e2", selectcolor="#16213e", activebackground="#1a1a2e", activeforeground="#e2e2e2").grid(row=0, column=1, sticky="w", padx=10, pady=5)
tk.Checkbutton(cb_frame, text="Numbers (0-9)", variable=use_digits, bg="#1a1a2e", fg="#e2e2e2", selectcolor="#16213e", activebackground="#1a1a2e", activeforeground="#e2e2e2").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Checkbutton(cb_frame, text="Symbols (%$#@!)", variable=use_symbols, bg="#1a1a2e", fg="#e2e2e2", selectcolor="#16213e", activebackground="#1a1a2e", activeforeground="#e2e2e2").grid(row=1, column=1, sticky="w", padx=10, pady=5)

# Action Buttons Container
btn_frame = tk.Frame(root, bg="#1a1a2e")
btn_frame.pack(pady=10)

gen_btn = tk.Button(btn_frame, text="Generate", command=generate_password, font=("Arial", 11, "bold"), bg="#00f5d4", fg="#1a1a2e", activebackground="#01c9ae", bd=0, padx=15, pady=6, cursor="hand2")
gen_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(btn_frame, text="Copy", command=copy_to_clipboard, font=("Arial", 11, "bold"), bg="#e91e63", fg="#ffffff", activebackground="#c2185b", bd=0, padx=15, pady=6, cursor="hand2")
copy_btn.grid(row=0, column=1, padx=10)

# Status Log Message
status_label = tk.Label(root, text="", font=("Arial", 10), bg="#1a1a2e", fg="#4caf50")
status_label.pack(pady=10)

# Initialize with a starting password on app load
generate_password()

root.mainloop()