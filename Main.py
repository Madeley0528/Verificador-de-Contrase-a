# main.py
from Verificador import verificar_minusculas, verificar_mayusculas, verificar_numeros, verificar_longitud

def evalua_la_contraseña(contraseña):
    cantidad = 0

    if verificar_minusculas(contraseña):
      cantidad += 25  
    if verificar_mayusculas(contraseña):
        cantidad+= 25  
    if verificar_numeros(contraseña):
        cantidad += 25  
    if verificar_longitud(contraseña):
        cantidad += 25

    return cantidad

# Solicitar la contraseña al usuario
contrasena = input("Ingres una contraseña para evaluar: ")

# Evaluar el puntaje de la contraseña
cantidad = evalua_la_contraseña(contrasena)

# Mostrar el nivel de seguridad de la contraseña
if cantidad == 100:
    print("Nivelación de seguridad: 100% (Muy segura)")
elif cantidad == 75:
    print("Nivelación de seguridad: 75% (Segura)")
elif cantidad == 50:
    print("Nivelación de seguridad: 50% (Moderada)")
elif cantidad == 25:
    print("Nivelación de seguridad: 25% (Débil)")
else:
    print("Nivelación de seguridad: 0% (Muy débil)")
