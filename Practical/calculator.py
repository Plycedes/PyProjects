import tkinter as tk

def calculate():
    try:
        # Get the input values from the entry fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        # Perform the selected operation
        if operation.get() == "Addition":
            result = num1 + num2
        elif operation.get() == "Subtraction":
            result = num1 - num2
        elif operation.get() == "Multiplication":
            result = num1 * num2
        elif operation.get() == "Division":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        
        # Update the result label
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Error: Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry fields for input
entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

# Create a dropdown menu for selecting the operation
operation = tk.StringVar(root)
operation.set("Addition")  # Default operation
dropdown_operation = tk.OptionMenu(root, operation, "Addition", "Subtraction", "Multiplication", "Division")
dropdown_operation.grid(row=0, column=2, padx=5, pady=5)

# Create a button to perform the calculation
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Create a label to display the result
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
