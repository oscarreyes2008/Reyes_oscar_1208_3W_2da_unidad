print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("oscar alonso reyes yañez_1208_3w:practica de vocales")
print(" ")#sirve para dejar un espacio a la hora de ejecutar

def es_vocal(caracter):#define la vocal como caracter
    vocales = 'aeiouAEIOU'#registra cuales son las vocales
    return caracter in vocales
print(" ")#sirve para dejar un espacio a la hora de ejecutar
def ingresar_letra():#te pide una letra o caracter
    """Solicita al usuario que ingrese un carácter."""
    letra = input("Ingresa un carácter: ")#te solicita un caracter
    
    if len(letra) == 1:  # Asegurarse de que solo se ingrese un carácter
        resultado = es_vocal(letra)
        return resultado
    else:
        print("Por favor, ingresa solo un carácter.")
        return None
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Ejemplo de uso
resultado = ingresar_letra()
if resultado is not None:
    print(f"¿Es una vocal? {resultado}")
print(" ")#sirve para dejar un espacio a la hora de ejecutar