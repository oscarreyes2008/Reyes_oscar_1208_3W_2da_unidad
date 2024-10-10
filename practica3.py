print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("oscar alonso reyes yañez_1208_3w:practica de factorial")
print(" ")#sirve para dejar un espacio a la hora de ejecutar

def factorial(n):#se define la variable
    if n < 0:
        return "Por favor, ingresa un entero positivo."#te pide un numero entero
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
print(" ")#sirve para dejar un espacio a la hora de ejecutar
numero = int(input("Ingresa un entero positivo: "))# Solicitar al usuario que ingrese un número
resultado = factorial(numero)#te dice que el resultado es la factorial del numeor que colocaste
print(f"El factorial de {numero} es {resultado}")#realiza la operacion para sacar la factorial
print(" ")#sirve para dejar un espacio a la hora de ejecutar



