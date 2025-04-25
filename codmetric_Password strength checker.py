import tkinter as tk
from tkinter import messagebox
import re

class PasswordComplexityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Complexity Checker") 
        self.root.geometry("500x400") 
        
        tk.Label(root, text="Enter Password:", font=("Arial", 14)).pack(pady=10)
        
        self.password_entry = tk.Entry(root, font=("Arial", 14), show="*")  
        self.password_entry.pack(pady=10)
        
        self.check_button = tk.Button(root, text="Check Password Strength", command=self.check_password_strength)
        self.check_button.pack(pady=20)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
        self.result_label.pack(pady=10)

    def check_password_strength(self):
        password = self.password_entry.get() 
        
        if len(password) < 8:
            self.result_label.config(text="Password must be at least 8 characters long.", fg="red")
            return
        
        if not re.search(r'[A-Z]', password):
            self.result_label.config(text="Password must contain at least one uppercase letter.", fg="red")
            return
        
        if not re.search(r'[a-z]', password):
            self.result_label.config(text="Password must contain at least one lowercase letter.", fg="red")
            return
        
        if not re.search(r'\d', password):
            self.result_label.config(text="Password must contain at least one digit.", fg="red")
            return
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            self.result_label.config(text="Moderate: Add a special character to make it stronger.", fg="orange")
            return

        self.result_label.config(text="Strong: Your password is strong!", fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordComplexityChecker(root)
    root.mainloop()
