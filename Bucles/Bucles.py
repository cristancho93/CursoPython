# Bucle While

import math
numero = int(input("Escriba un numero: \n"))

while numero < 0:
    print("Por favor ingrese un numero positivo")
    numero = int(input("Escriba un numero positivo: \n"))

print(f"El resultado de raiz cuadrada es: {math.sqrt(numero)}")