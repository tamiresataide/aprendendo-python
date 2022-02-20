hora = int(input("Olá, que horas são? "))
if 0 <= hora <=11:
    print("Bom dia!")
elif 12 <= hora <= 17:
    print("Boa tarde!")
else:
    print("Boa noite!")