import tkinter as tk

def generar_contrasena():
        longitud1 = int(longitud.get())
        import random 
        import string
        contrasena = ''
        for i in range(longitud1):
            contrasena += random.choice(string.ascii_letters + string.digits + string.punctuation)
        return var.set(contrasena)

ventana = tk.Tk()
ventana.title("Generador de contraseñas")
ventana.geometry("400x400")
ventana.configure(bg="white")
var = tk.StringVar()

elemento = tk.Label(ventana, text="Generador de contraseñas", bg="black", fg="white")
elemento.pack(padx = 10, pady = 10, ipadx=5, ipady=5, fill=tk.X)
longitud = tk.Entry(ventana)
longitud.pack(padx = 10, pady = 10, ipadx=5, ipady=5,fill=tk.X)

boton = tk.Button(ventana, text="Generar contraseña", fg="blue", command=generar_contrasena)
boton.pack(side=tk.TOP)
op =tk.Label(ventana, bg = "white", textvariable=var)

res = tk.Label(ventana, text="Tu contraseña es: ", bg="white")
res.pack(padx = 10, pady = 10, ipadx=5, ipady=5, fill=tk.X)


ventana.mainloop()

print (generar_contrasena(8))