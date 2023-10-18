import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    
    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4 characters")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Generated Password: " + password)

app = tk.Tk()
app.title("Password Generator")

length_label = tk.Label(app, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(app)
length_entry.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
