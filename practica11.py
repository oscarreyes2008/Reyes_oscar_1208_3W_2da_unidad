print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("oscar alonso reyes yañez_1208_3w:practica de distancia entre 2 puntos")
print(" ")#sirve para dejar un espacio a la hora de ejecutar

def distancia_dirigida():
    # Solicitar las coordenadas del primer punto
    x1 = float(input("Ingresa la coordenada x del primer punto: "))#primer coordenada
    y1 = float(input("Ingresa la coordenada y del primer punto: "))#segunda coordenada
    
    # Solicitar las coordenadas del segundo punto
    x2 = float(input("Ingresa la coordenada x del segundo punto: "))#primer coordenada del segundo punto
    y2 = float(input("Ingresa la coordenada y del segundo punto: "))#segunda coordenada del ssegundo punto
    
    # Calcular la distancia dirigida
    distancia = (x2 - x1, y2 - y1)
    
    return distancia
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Ejemplo de uso
resultado = distancia_dirigida()
print(f"La distancia dirigida entre estos puntos es: {resultado}")#te dice que la distancia de los dos puntos es:
print(" ")#sirve para dejar un espacio a la hora de ejecutar