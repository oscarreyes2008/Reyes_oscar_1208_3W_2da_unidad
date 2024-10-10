print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("oscar alonso reyes yañez_1208_3w:practica de gmail")
print(" ")#sirve para dejar un espacio a la hora de ejecutar
def es_email_valido(email):#define la variable
    return '@' in email#verifica si lleva el arroba en el correo
print(" ")#sirve para dejar un espacio a la hora de ejecutar
def capturar_email():
    """Captura una dirección de correo electrónico y verifica su validez."""
    email = input("Ingresa tu dirección de email: ")
    
    if es_email_valido(email):
        print("La dirección de email es válida.")#te dice si es valido
    else:
        print("La dirección de email no es válida. Debe contener '@'.")#te dice que no es valido ya que no tiene el @
print(" ")#sirve para dejar un espacio a la hora de ejecutar
capturar_email()
print(" ")#sirve para dejar un espacio a la hora de ejecutar