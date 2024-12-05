import math
def encriptar(texto, clave):
    """
    Encripta el texto utilizando un desplazamiento (clave).
    
    La función toma un texto y lo encripta desplazando cada uno de sus caracteres en la tabla ASCII
    por un valor definido en la `clave`. Luego, guarda el texto encriptado en un archivo de texto.

    Parámetros:
    texto (str): El texto que se quiere encriptar.
    clave (int): El valor que se usará para desplazar los caracteres en la tabla ASCII.

    El texto encriptado se guarda en un archivo llamado "mensaje_encriptado.txt".
    """
    
    # Se crea una variable para almacenar el texto encriptado
    texto_encriptado = ""

    # Iteramos sobre cada carácter del texto original
    for char in texto:
        # Convertimos el carácter en su código ASCII (mediante ord(char)),
        # sumamos la clave para desplazarlo y luego convertimos el valor
        # de vuelta a un carácter (mediante chr()) y lo agregamos al texto encriptado
        texto_encriptado += chr(ord(char) + clave)
    
    # Guardamos el texto encriptado en un archivo llamado "mensaje_encriptado.txt"
    with open("mensaje_encriptado.txt", mode="w", encoding='utf-8') as archivo:
        archivo.write(texto_encriptado)


def desencriptar(texto, clave):
    """
    Desencripta el texto utilizando un desplazamiento (clave).
    
    La función toma un texto encriptado y lo desencripta al revertir el desplazamiento 
    de caracteres que se realizó al encriptarlo. Esto se hace restando el valor de la clave 
    al código ASCII de cada carácter en el texto original.

    Parámetros:
    texto (str): El texto que se quiere desencriptar, que se ha encriptado previamente 
                 mediante desplazamiento de caracteres.
    clave (int): El valor que se usó para desplazar los caracteres al encriptarlos.

    Retorna:
    str: El texto desencriptado, es decir, el texto original antes de la encriptación.
    """
    
    # Se crea una variable para almacenar el texto desencriptado
    texto_desencriptado = ""

    # Iteramos sobre cada carácter del texto encriptado
    for char in texto:
        # Convertimos el carácter en su código ASCII (mediante ord(char)), restamos la clave
        # para revertir el desplazamiento, y luego lo convertimos de nuevo en un carácter
        # (mediante chr()) para agregarlo al texto desencriptado
        texto_desencriptado += chr(ord(char) - clave)
    
    # Al final, devolvemos el texto desencriptado
    return texto_desencriptado

# Clave de encriptado
clave = int((math.pi * 1000) % 256)



with open("mensaje_encriptado.txt", "r", encoding="utf-8") as archivo:
    texto_leido = archivo.read() 

texto_desencriptado = desencriptar(texto_leido, clave)

print(texto_desencriptado)