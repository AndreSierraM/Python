import tkinter as tk

entry.insert(0, "Hola mundo!")
entry.place(x=50, y=50)
button = ttk.Button(text="Obtener texto", command=lambda: print(entry.get()))
button.place(x=50, y=100)