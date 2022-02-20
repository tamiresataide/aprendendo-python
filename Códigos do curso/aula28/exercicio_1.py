num = input("Digite um número: ")
while not num.isnumeric():
    num = input("Por favor digite um número inteiro: ")
num = int(num)
if (num % 2) == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é impar")
