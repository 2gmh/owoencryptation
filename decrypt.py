import random
import string
mensaje_encriptado = "owowowowoowo owowowo owoo owowowow ow owowowow ow  oowwo ow oowowowo owowo oow"
def desencriptar(mensaje_encriptado):
    codigos_inversos = {'ow': 'a', 'oowwwwo': 'b', 'owowowowoowo': 'c', 'oowwwo': 'd', 'ow': 'e', 'owowowowowo': 'f', 'oowowowo': 'g', 'owowowo': 'h', 'owowo': 'i', 'owoooow': 'j', 'oowowwo': 'k', 'owowowow': 'l', 'oowoow': 'm', 'oowwo': 'n', 'oow': 'o', 'owowowow': 'p', 'oowowoow': 'q', 'owowo': 'r', 'owowow': 's', 'o': 't', 'owoo': 'u', 'owowoo': 'v', 'owooo': 'w', 'oowowow': 'x', 'oowowo': 'y', 'oowoow': 'z', 'uwowu1oowuw': '1', 'uwowu2oowuw': '2', 'uwowu3oowuw': '3', 'uwowu4oowuw': '4', 'uwowu5oowuw': '5', 'uwowu6oowuw': '6', 'uwowu7oowuw': '7', 'uwowu8oowuw': '8', 'uwowu9oowuw': '9', 'uwowu0oowuw': '0', 'oowooowow': '.', 'oowooowoowoo': ':', 'oowowoowow': '-', 'owoooowowo': '_', 'owoowo': '?', 'owooowo': '¿', 'oowooowo': '!', 'owooowoo': '¡'}

    mensaje_desencriptado = ''
    codigo_actual = ''
    for letra in mensaje_encriptado:
        if letra == ' ':
            mensaje_desencriptado += letra
            codigo_actual = ''
        else:
            codigo_actual += letra
            if codigo_actual in codigos_inversos:
                mensaje_desencriptado += codigos_inversos[codigo_actual]
                codigo_actual = ''
    
    return mensaje_desencriptado

mensaje_desencriptado = desencriptar(mensaje_encriptado)
print("Mensaje desencriptado: ", mensaje_desencriptado)

