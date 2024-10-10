print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("oscar alonso reyes yañez_1208_3w:practica de longitud de la palabra")
print(" ")#sirve para dejar un espacio a la hora de ejecutar

def longitud_ultima_palabra():#define la variable
    # Solicitar al usuario que ingrese un string
    s = input("Ingresa una frase: ")
    
    # Dividir el string en palabras, eliminando múltiples espacios
    palabras = s.split()
    
    # Verificar si hay palabras
    if palabras:
        # Regresar la longitud de la última palabra
        return len(palabras[-1])
    else:
        # Si no hay palabras, regresar 0
        return 0
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Ejemplo de uso
longitud = longitud_ultima_palabra()
print(f"La longitud de la última palabra es: {longitud}")#te dice la longuitud de la palabra
print(" ")#sirve para dejar un espacio a la hora de ejecutar

