# Programa para generar contraseñas  aleatorias
from tkinter import *
# Función para generar contraseñas
def generar_contrasena(longitud):
        import random 
        import string
        contrasena = ''
        for i in range(longitud):
            contrasena += random.choice(string.ascii_letters + string.digits + string.punctuation)
        return contrasena
def __main__(): 
    longitud = int(input('Ingresa la longitud de la contraseña: '))
    contrasena = generar_contrasena(longitud)
    print('Tu contraseña es: ', contrasena)
    
if __name__ == '__main__':
    __main__()
    

