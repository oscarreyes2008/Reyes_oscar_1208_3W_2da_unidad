print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("oscar alonso reyes yañez_1208_3w:practica de el area del circulo y altura del cilindro")
print(" ")#sirve para dejar un espacio a la hora de ejecutar
import math
print(" ")#sirve para dejar un espacio a la hora de ejecutar
def area_circulo(radio):#defne la variable
    return math.pi * (radio ** 2)
print(" ")#sirve para dejar un espacio a la hora de ejecutar
def volumen_cilindro(radio, altura):
    """Calcula el volumen de un cilindro utilizando el área del círculo."""
    area = area_circulo(radio)
    return area * altura
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Ejemplo de uso
radio = float(input("Ingresa el radio del círculo: "))
altura = float(input("Ingresa la altura del cilindro: "))
print(" ")#sirve para dejar un espacio a la hora de ejecutar
area = area_circulo(radio)
volumen = volumen_cilindro(radio, altura)
print(" ")#sirve para dejar un espacio a la hora de ejecutar
print(f"El área del círculo es: {area:.2f}")#te dice que cual es el area
print(f"El volumen del cilindro es: {volumen:.2f}")#te dice cual es el volumen del cilindro
print(" ")#sirve para dejar un espacio a la hora de ejecutar