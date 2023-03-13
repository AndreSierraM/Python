# Convertir el número en binario a decimal
num_binario = '0100000010101001001100000000000000000000000000000000000000000000'
signo = int(num_binario[0])
exponente = int(num_binario[1:12], 2) - 1023
mantisa_binaria = '1' + num_binario[12:]
mantisa = sum(int(mantisa_binaria[i]) * 2**-(i+1) for i in range(52))
num_decimal = (-1)**signo * (1 + mantisa) * 2**exponente

print('El número decimal es:', num_decimal)

# Encontrar el inmediato mayor
if signo == 0:
    mantisa_binaria = bin(int(mantisa_binaria, 2) + 1)[2:].zfill(52)
else:
    mantisa_binaria = bin(int(mantisa_binaria, 2) - 1)[2:].zfill(52)

inmediato_mayor = (-1)**signo * (1 + sum(int(mantisa_binaria[i]) * 2**-(i+1) for i in range(52))) * 2**exponente
print('El inmediato mayor es:', inmediato_mayor)

# Encontrar el inmediato menor
if signo == 0 and mantisa_binaria != '0000000000000000000000000000000000000000000000000000000000000000001':
mantisa_binaria = bin(int(mantisa_binaria, 2) - 1)[2:].zfill(52)
else:
mantisa_binaria = bin(int(mantisa_binaria, 2) + 1)[2:].zfill(52)

inmediato_menor = (-1)signo * (1 + sum(int(mantisa_binaria[i]) * 2-(i+1) for i in range(52))) * 2**exponente
print('El inmediato menor es:', inmediato_menor)
