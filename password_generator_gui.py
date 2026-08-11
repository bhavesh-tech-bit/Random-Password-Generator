import tkinter as tk
from tkinter import messagebox
import pyperclip

password_history = []
from password_generator import generate_password



def check_password_strength(password):

    strength = 0

    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1

 
    if any(c.isupper() for c in password):
        strength += 1

    if any(c.islower() for c in password):
        strength += 1

    if any(c.isdigit() for c in password):
        strength += 1

    if any(not c.isalnum() for c in password):
        strength += 1

    if strength <= 3:
        return "Weak"

    elif strength <= 5:
        return "Medium"

    else:
        return "Strong"


def generate_password_button():
    try:
        length = int(length_spinbox.get())

        if length < 8:
            messagebox.showerror(
                "Error",
                "Password length must be at least 8."
                 )
            return

        password = generate_password(
            length,
            uppercase_var.get(),
            lowercase_var.get(),
            numbers_var.get(),
            symbols_var.get(),
            exclude_ambiguous_var.get()
             )

       
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)


        password_history.insert(0, password)

     
        if len(password_history) > 5:
            password_history.pop()

      
        history_listbox.delete(0, tk.END)

        for pwd in password_history:
            history_listbox.insert(tk.END, pwd)

  
        pyperclip.copy(password)

        messagebox.showinfo(
            "Success",
            "Password generated and copied to clipboard!"
             )

     
        strength = check_password_strength(password)
        strength_label.config(
            text=f"Password Strength: {strength}"
             )

    except ValueError as e:
        messagebox.showerror("Error", str(e))



def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first.")


def clear_password():
    password_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("700x550")  
root.resizable(False, False)

title = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)


length_frame = tk.Frame(root)
length_frame.pack(pady=5)

tk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)

length_spinbox = tk.Spinbox(
    length_frame,
    from_=8,
    to=50,
    width=5
)
length_spinbox.pack(side=tk.LEFT, padx=10)


uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Uppercase Letters",
    variable=uppercase_var
).pack(anchor="w", padx=60)

tk.Checkbutton(
    root,
    text="Lowercase Letters",
    variable=lowercase_var
).pack(anchor="w", padx=60)

tk.Checkbutton(
    root,
    text="Numbers",
    variable=numbers_var
).pack(anchor="w", padx=60)

tk.Checkbutton(
    root,
    text="Symbols",
    variable=symbols_var
).pack(anchor="w", padx=60)



exclude_ambiguous_var = tk.BooleanVar(value=False)

tk.Checkbutton(
    root,
    text="Exclude Ambiguous Characters (0, O, l, 1)",
    variable=exclude_ambiguous_var
    ).pack(anchor="w", padx=60)


button_frame = tk.Frame(root)
button_frame.pack(pady=20)

generate_button = tk.Button(
    button_frame,
    text="Generate Password",
    command=generate_password_button,
    width=15
    )
generate_button.grid(row=0, column=0, padx=5)

copy_button = tk.Button(
    button_frame,
    text="Copy Password",
    command=copy_password,
    width=15
    )
copy_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_password,
    width=15
    )
clear_button.pack()


tk.Label(
    root,
    text="Generated Password:",
    font=("Arial", 11, "bold")
    ).pack(pady=10)

password_entry = tk.Entry(
    root,
    width=45,
    font=("Arial", 12),
    justify="center"
      )
password_entry.pack(pady=5)

strength_label = tk.Label(
    root,
    text="Password Strength:",
    font=("Arial", 11, "bold")
    )
strength_label.pack(pady=10)

history_label = tk.Label(
    root,
    text="Last 5 Generated Passwords",
    font=("Arial", 11, "bold")
     )
history_label.pack(pady=10)

history_listbox = tk.Listbox(
    root,
    width=45,
    height=5
   )
history_listbox.pack()

root.mainloop()