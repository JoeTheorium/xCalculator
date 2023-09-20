import tkinter as tk
from sympy import sqrt, factorial
from calcs import (
    add,
    subtract,
    multiply,
    divide,
    raise_to_power,
    calculate_square_root,
    calculate_factorial,
)


class xCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("xCalculator")

        self.result_var = tk.StringVar()

        # RESULT SCREEN
        self.result_display = tk.Entry(
            root, textvariable=self.result_var, font=("Arial", 16), justify="right")
        # Create a result display
        self.result_display.grid(row=0, column=0, columnspan=4)

        # BUTTONS
        button_texts = [
            # Define buttons with text and positions
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("√", 1, 4), ("^", 2, 4), ("!", 3, 4), ("C", 4, 4)
        ]

        for (text, row, col) in button_texts:
            # Create and place buttons
            button = tk.Button(root, text=text, font=(
                "Arial", 16), command=lambda t=text: self.on_button_click(t))
            # Create and position buttons
            button.grid(row=row, column=col, padx=10, pady=10)

    def on_button_click(self, value):
        if value == "=":
            try:
                # Evaluate and display the result when "=" is pressed
                result = eval(self.result_var.get())  # Evaluate the expression
                self.result_var.set(result)  # Set the result to the display
            except Exception as e:
                self.result_var.set("Error")  # Handle errors
        elif value == "√":
            try:
                # Calculate square root and update the result display
                # Get the current text from the display
                current_text = float(self.result_var.get())
                result = self.calculate_square_root(
                    current_text)  # Calculate the square root
                self.result_var.set(result)  # Set the result to the display
            except Exception as e:
                self.result_var.set("Error")  # Handle errors
        elif value == "^":
            # Append "**" to the current expression for exponentiation
            # Add exponentiation operator
            self.result_var.set(self.result_var.get() + "**")
        elif value == "!":
            try:
                # Calculate factorial and update the result display
                # Get the current text from the display
                current_text = int(self.result_var.get())
                result = self.calculate_factorial(
                    current_text)  # Calculate the factorial
                self.result_var.set(result)  # Set the result to the display
            except Exception as e:
                self.result_var.set("Error")  # Handle errors
        elif value == "C":
            # Clear the result display when "C" is pressed
            self.result_var.set("")
        else:
            # Append the button's value to the current expression
            current_text = self.result_var.get()  # Get the current text from the display
            new_text = current_text + value  # Append the clicked button value
            # Update the display with the new text
            self.result_var.set(new_text)

    def calculate_square_root(self, number):
        if number >= 0:
            return round(sqrt(number), 4)  # Calculate and round square root
        else:
            return "Error"  # Handle errors for negative numbers

    def calculate_factorial(self, number):
        if number >= 0:
            # Calculate factorial and return as a string
            return str(factorial(number))
        else:
            return "Error"  # Handle errors for negative numbers


def main():
    root = tk.Tk()
    app = xCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
