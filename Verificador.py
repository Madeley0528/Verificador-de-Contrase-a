# verificador.py

def verificar_minusculas(contraseña):
    for caracter in contraseña:
        if caracter >= 'a' and caracter <= 'z': 
         return True
    return False

def verificar_mayusculas(contraseña):
    for caracter in contraseña:
        if caracter >= 'A' and caracter <= 'Z':  
            return True
    return False

def verificar_numeros(contraseña):
    for caracter in contraseña:
        if caracter >= '0' and caracter <= '9': 
            return True
    return False

def verificar_longitud(contraseña):
    if len(contraseña) > 8:
        return True
    return False
