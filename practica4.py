print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("oscar alonso reyes yañez_1208_3w:practica de iva")
print(" ")#sirve para dejar un espacio a la hora de ejecutar

def calcular_total_con_iva():
    
    cantidad_sin_iva = float(input("Ingresa la cantidad sin IVA: "))# Solicitar la cantidad sin IVA
    
    
    porcentaje_iva = float(input("Ingresa el porcentaje de IVA: "))# Solicitar el porcentaje de IVA
    
    
    iva = (porcentaje_iva / 100) * cantidad_sin_iva# Calcular el total de la factura
    total_con_iva = cantidad_sin_iva + iva#le suma el iva a el total
    
    return total_con_iva

# Ejemplo de uso
total = calcular_total_con_iva()
print(f"El total de la factura después del IVA es: {total:.2f}")
