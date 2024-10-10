print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("oscar alonso reyes yañez_1208_3w:practica de tres numeros")
print(" ")#sirve para dejar un espacio a la hora de ejecutar

def mayor_de_tres():#define la variable
    num1 = float(input("Ingresa el primer número: "))#te pide que ingreses un numero
    num2 = float(input("Ingresa el segundo número: "))#te pide otro numero
    num3 = float(input("Ingresa el tercer número: "))#te pide un tercer numero
    
    return max(num1, num2, num3)#sirve para regresar el mayor de los 3
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Ejemplo de uso
resultado = mayor_de_tres()
print(f"El mayor de los tres números es: {resultado}")#mensaje que se muestra a la hora de ejecutar
print(" ")#sirve para dejar un espacio a la hora de ejecutar