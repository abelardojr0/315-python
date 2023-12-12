def contar_caracteres(texto):
    # return len(texto)
    contador = 0
    for letra in texto:
        contador +=1
    return contador


def contar_vogais(texto):
    contador = 0
    for letra in texto:
        if letra in "aeiouáâãéêíóôõú":
            contador +=1
    return contador

def contar_consoates(texto):
    contador = 0
    for letra in texto:
        if letra in "bcdfghjklmnpqrstvxywz":
            contador +=1
    return contador


def contar_vazios(texto):
    contador = 0
    for letra in texto:
        if letra == " ":
            contador +=1
    return contador