import tkinter as tk

from tkinter import messagebox

def validate_login():

 username = entry_username.get()

 password = entry_password.get()
[10/26, 11:52 AM] ..: label_username = tk.Label(root, text="Username:")

label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)

entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")

label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")

entry_password.grid(row=1, column=1, padx=10, pady=10)
[10/26, 11:53 AM] ..: button_login = tk.Button(root, text="Login", 

command=validate_login)

button_login.grid(row=2, column=1, pady=10)

root.mainloop()
