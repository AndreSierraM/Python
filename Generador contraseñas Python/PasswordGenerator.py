import random
import string
import tkinter as tk


class PasswordGenerator:
    def __init__(self, master): # master es la ventana principal
        self.master = master # self.master es la ventana principal
        self.master.title("Generador de Contraseñas") # título de la ventana
        self.master.geometry("300x200") # ancho x alto
        
        self.label = tk.Label(self.master, text="Longitud de la contraseña:") # texto
        self.label.pack() # empaquetar el texto
        
        self.entry = tk.Entry(self.master) # entrada de texto
        self.entry.pack() # empaquetar la entrada de texto
        
        self.button = tk.Button(self.master, text="Generar Contraseña", command=self.generate_password) # botón
        self.button.pack() # empaquetar el botón
        
        self.password_label = tk.Label(self.master, text="") # texto
        self.password_label.pack() # empaquetar el texto
    
    def generate_password(self): # función para generar la contraseña
        length = int(self.entry.get()) # obtener el valor de la entrada de texto
        chars = string.ascii_letters + string.digits + string.punctuation # caracteres
        password = "".join(random.choice(chars) for _ in range(length)) # contraseña
        self.password_label.config(text=password) # configurar el texto

root = tk.Tk() # ventana principal
password_generator = PasswordGenerator(root) # instanciar la clase
root.mainloop() # bucle principal
