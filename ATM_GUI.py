import tkinter as tk
from tkinter import messagebox

# Initial Setup
balance = 1000.0
pin_code = "1234"

# Tkinter Window
window = tk.Tk()
window.title("ATM Machine")
window.geometry("350x450")
window.config(bg="#003366")

# Global Variables
pin_entry = tk.StringVar()
amount_entry = tk.StringVar()
current_action = None

# Function Definitions
def verify_pin():
    if pin_entry.get() == pin_code:
        display_menu()
    else:
        messagebox.showerror("Access Denied", "Incorrect PIN")

def display_menu():
    clear_screen()
    tk.Label(window, text="Welcome!", bg="#003366", fg="white", font=("Arial", 16)).pack(pady=10)
    tk.Button(window, text="Check Balance", command=check_balance, width=20, bg="#00cc99", fg="white").pack(pady=5)
    tk.Button(window, text="Deposit", command=deposit_menu, width=20, bg="#3399ff", fg="white").pack(pady=5)
    tk.Button(window, text="Withdraw", command=withdraw_menu, width=20, bg="#ff9933", fg="white").pack(pady=5)
    tk.Button(window, text="Change PIN", command=change_pin_menu, width=20, bg="#cc6699", fg="white").pack(pady=5)
    tk.Button(window, text="Exit", command=window.quit, width=20, bg="#cccccc", fg="black").pack(pady=5)

def check_balance():
    messagebox.showinfo("Balance", f"Your current balance is ₹{balance:.2f}")

def deposit_menu():
    prepare_transaction("Deposit Amount:", "deposit")

def withdraw_menu():
    prepare_transaction("Withdraw Amount:", "withdraw")

def change_pin_menu():
    clear_screen()
    tk.Label(window, text="Enter New PIN:", bg="#003366", fg="white", font=("Arial", 12)).pack(pady=10)
    new_pin = tk.Entry(window, show="*", font=("Arial", 12))
    new_pin.pack(pady=5)
    tk.Button(window, text="Update PIN", command=lambda: update_pin(new_pin.get()), bg="#cc6699", fg="white").pack(pady=10)

def update_pin(new_value):
    global pin_code
    if len(new_value) == 4 and new_value.isdigit():
        pin_code = new_value
        messagebox.showinfo("Success", "PIN successfully updated.")
        display_menu()
    else:
        messagebox.showerror("Error", "PIN must be 4 digits.")

def prepare_transaction(label_text, action_type):
    global current_action
    current_action = action_type
    clear_screen()
    tk.Label(window, text=label_text, bg="#003366", fg="white", font=("Arial", 12)).pack(pady=10)
    amount = tk.Entry(window, textvariable=amount_entry, font=("Arial", 12))
    amount.pack(pady=5)
    tk.Button(window, text="Submit", command=process_transaction, bg="#3399ff", fg="white").pack(pady=10)

def process_transaction():
    global balance
    try:
        amount = float(amount_entry.get())
        if current_action == "deposit":
            balance += amount
            messagebox.showinfo("Deposited", f"₹{amount:.2f} deposited.\nNew Balance: ₹{balance:.2f}")
        elif current_action == "withdraw":
            if amount <= balance:
                balance -= amount
                messagebox.showinfo("Withdrawn", f"₹{amount:.2f} withdrawn.\nNew Balance: ₹{balance:.2f}")
            else:
                messagebox.showerror("Error", "Insufficient funds.")
        amount_entry.set("")
        display_menu()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")

def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()

# PIN Entry UI
tk.Label(window, text="Enter PIN", bg="#003366", fg="white", font=("Arial", 16)).pack(pady=20)
tk.Entry(window, textvariable=pin_entry, show="*", font=("Arial", 14)).pack(pady=10)
tk.Button(window, text="Enter", command=verify_pin, width=15, bg="#00cc99", fg="white").pack(pady=10)

window.mainloop()