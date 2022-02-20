frase = 'o rato roeu a roupa do rei de roma'
contador = 0
nova = ''
user = input("Digite uma letra: ")
while contador < len(frase):
    letra = frase[contador]
    if letra == user:
        nova += user.upper()
    else:
        nova += letra
    contador += 1
print(nova)
