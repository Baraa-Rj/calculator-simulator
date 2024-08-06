import tkinter as tk
from tkinter import messagebox


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Error! Division by zero.")
    return n1 / n2


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {num1} {operation} {num2} = {result}")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="First Number:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

tk.Label(root, text="Operation:").grid(row=2, column=0)
operation_var = tk.StringVar(value="+")
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1)

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2)

root.mainloop()
