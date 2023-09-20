import tkinter as tk
from sympy import sqrt, factorial
from calcs import (
    sumar,
    restar,
    multiplicar,
    dividir,
    elevar_potencia,
    calcular_raiz_cuadrada,
    calcular_factorial,
)


class xCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("xCalculator")

        self.result_var = tk.StringVar()

        # Pantalla de resultado
        self.result_display = tk.Entry(
            root, textvariable=self.result_var, font=("Arial", 16), justify="right")
        self.result_display.grid(row=0, column=0, columnspan=4)

        # Botones
        button_texts = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("√", 1, 4), ("^", 2, 4), ("!", 3, 4)
        ]

        for (text, row, col) in button_texts:
            button = tk.Button(root, text=text, font=(
                "Arial", 16), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=10, pady=10)

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif value == "√":
            try:
                current_text = float(self.result_var.get())
                result = self.calculate_square_root(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif value == "^":
            self.result_var.set(self.result_var.get() + "**")
        elif value == "!":
            try:
                current_text = int(self.result_var.get())
                result = self.calculate_factorial(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + value
            self.result_var.set(new_text)

    def calculate_square_root(self, number):
        if number >= 0:
            return round(sqrt(number), 4)
        else:
            return "Error"

    def calculate_factorial(self, number):
        if number >= 0:
            return str(factorial(number))
        else:
            return "Error"


def main():
    root = tk.Tk()
    app = xCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
