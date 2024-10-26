import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Simple validation - you can modify this as needed
    if username == "admin" and password == "password":
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")  # Set window size

# Create and place username elements
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Create and place password elements
label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Create and place login button
button_login = tk.Button(root, text="Login", command=validate_login)
button_login.grid(row=2, column=1, pady=10)

# Start the main event loop
root.mainloop()
