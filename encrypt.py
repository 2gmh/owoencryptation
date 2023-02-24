import random
import string

def encriptar(mensaje):
    codigos = {'a': 'ow', 'b': 'oowwwwo', 'c': 'owowowowoowo', 'd': 'oowwwo', 'e': 'ow', 'f': 'owowowowowo', 'g': 'oowowowo', 'h': 'owowowo', 'i': 'owowo', 'j': 'owoooow', 'k': 'oowowwo', 'l': 'owowowow', 'm': 'oowoow', 'n': 'oowwo', 'o': 'oow', 'p': 'owowowow', 'q': 'oowowoow', 'r': 'owowo', 's': 'owowow', 't': 'o', 'u': 'owoo', 'v': 'owowoo', 'w': 'owooo', 'x': 'oowowow', 'y': 'oowowo', 'z': 'oowoow', '1': 'uwowu1oowuw', '2': 'uwowu2oowuw', '3': 'uwowu3oowuw', '4': 'uwowu4oowuw', '5': 'uwowu5oowuw', '6': 'uwowu6oowuw', '7': 'uwowu7oowuw', '8': 'uwowu8oowuw', '9': 'uwowu9oowuw', '0': 'uwowu0oowuw', '.': 'oowooowow', ':': 'oowooowoowoo', '-': 'oowowoowow', '_': 'owoooowowo', '?': 'owoowo', '¿': 'owooowo', '!': 'oowooowo', '¡': 'owooowoo'}
    mensaje = mensaje.lower()
    mensaje_encriptado = ''
    for letra in mensaje:
        if letra in codigos:
            mensaje_encriptado += codigos[letra] + ' '
        elif letra.isdigit():
            mensaje_encriptado += "uwowu" + letra + "oowuw" + ' '
        elif letra == " ":
            mensaje_encriptado += " "
        else:
            mensaje_encriptado += letra + ' '

    # Si la cadena encriptada no está vacía, devolverla
    if mensaje_encriptado:
        return mensaje_encriptado.strip()  # Eliminar posible espacio al final
    else:
        return None


mensaje = "Chupala negro"
mensaje_encriptado = encriptar(mensaje)

print("Mensaje original: ", mensaje)
print("Mensaje encriptado: ", mensaje_encriptado)
