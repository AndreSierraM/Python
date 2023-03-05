import random
import string
import tkinter as tk


class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Generador de Contraseñas")
        self.master.geometry("300x200")
        
        self.label = tk.Label(self.master, text="Longitud de la contraseña:")
        self.label.pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        
        self.button = tk.Button(self.master, text="Generar Contraseña", command=self.generate_password)
        self.button.pack()
        
        self.password_label = tk.Label(self.master, text="")
        self.password_label.pack()
    
    def generate_password(self):
        length = int(self.entry.get())
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        self.password_label.config(text=password)

root = tk.Tk()
password_generator = PasswordGenerator(root)
root.mainloop()