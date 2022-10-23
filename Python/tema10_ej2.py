import tkinter
from tkinter import ttk

def main():
    root = tkinter.Tk()
    lista = ["Rojo", "Azul", "Amarillo", "Verde", "Violeta", "Naranja"]
    lista_items = tkinter.StringVar(value=lista)
    listbox = tkinter.Listbox(root, height=10, listvariable=lista_items)
    listbox.pack()
    label = tkinter.Label(root, text="Lista de colores")
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
