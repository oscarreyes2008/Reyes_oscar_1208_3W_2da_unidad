print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("oscar alonso reyes yañez_1208_3w:practica de suma y multiplicacion")
print(" ")#sirve para dejar un espacio a la hora de ejecutar

def sum(numeros):#define la variable
    total = 0
    for num in numeros:
        total += num
    return total#te da el total 
print(" ")#sirve para dejar un espacio a la hora de ejecutar
def multip(numeros):#define los valores
    """Devuelve el producto de todos los números en la lista."""
    total = 1
    for num in numeros:
        total *= num
    return total
print(" ")#sirve para dejar un espacio a la hora de ejecutar
def ingresar_numeros():
    """Solicita al usuario que ingrese una lista de números."""
    numeros = input("Ingresa números separados por espacios: ")#te pide 3 numeros separados por un espacio para hacer la operacion
    lista_numeros = [float(num) for num in numeros.split()]
    return lista_numeros
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Ejemplo de uso
lista = ingresar_numeros()
resultado_suma = sum(lista)#realiza la suma
resultado_multiplicacion = multip(lista)#realiza la multiplicacion
print(" ")#sirve para dejar un espacio a la hora de ejecutar
print(f"La suma es: {resultado_suma}")          # Muestra la suma
print(f"La multiplicación es: {resultado_multiplicacion}")  # Muestra la multiplicación
print(" ")#sirve para dejar un espacio a la hora de ejecutar