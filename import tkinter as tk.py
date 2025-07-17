import tkinter as tk
from tkinter import ttk, messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry_operand1.get())
        num2 = float(entry_operand2.get())
        op = operator.get()

        if op == '+':
            result.set(num1 + num2)
        elif op == '-':
            result.set(num1 - num2)
        elif op == '*':
            result.set(num1 * num2)
        elif op == '/':
            result.set(num1 / num2 if num2 != 0 else "Error")
        else:
            result.set("Unknown")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Function to clear all fields
def clear_all():
    entry_operand1.delete(0, tk.END)
    entry_operand2.delete(0, tk.END)
    operator.set('+')
    result.set("")

# GUI setup
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x250")

# Operand 1
tk.Label(window, text="Operand 1").pack()
entry_operand1 = tk.Entry(window)
entry_operand1.pack()

# Operand 2
tk.Label(window, text="Operand 2").pack()
entry_operand2 = tk.Entry(window)
entry_operand2.pack()

# Operator dropdown
tk.Label(window, text="Operator").pack()
operator = ttk.Combobox(window, values=["+", "-", "*", "/"])
operator.pack()
operator.set("+")

# Result field
tk.Label(window, text="Result").pack()
result = tk.StringVar()
entry_result = tk.Entry(window, textvariable=result, state="readonly")
entry_result.pack()

# Buttons
tk.Button(window, text="Calculate", command=calculate).pack(pady=5)
tk.Button(window, text="Clear All", command=clear_all).pack()

window.mainloop()