from gui import xCalculator
import tkinter as tk  # Importo la biblioteca "tkinter" para crear la ventana principal


def main():
    root = tk.Tk()  # Creo la ventana principal
    # Creo una instancia de "xCalculator" y paso 'root' como argumento
    app = xCalculator(root)
    root.mainloop()  # Inicio el bucle principal de la interfaz gráfica


if __name__ == "__main__":
    main()
