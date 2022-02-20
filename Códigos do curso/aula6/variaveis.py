import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)
 
###########
#  USAGE  #
###########
 
# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True

# False
print(is_number('123a'))  # False

print("Calculadora de IMC \nInsira seus dados \n")
nome = input("Nome: ")
while len(nome) < 2 or is_number(nome):
    nome = input("Por favor, digite um nome válido: ")
idade = input("Data de nascimento (dd/mm/aaaa): ")
while len(idade) != 10:
    idade = input("Por favor, digite uma data válida (dd/mm/aaaa): ")
altura = input("Altura: ")
while not is_float(altura):
    altura = (input("Por favor, digite uma altura válida: "))
altura = float(altura)
peso = input("Peso: ")
while not is_number(peso):
    peso = input("Por favor digite um peso válido: ")
peso = float(peso)
imc = (peso / (altura * altura))
ano = 2021 - int(idade[-4:])
print(f'{nome} tem {idade} anos, {altura:.2f}m de altura e pesa {peso:.2f}kg. \nO IMC de {nome} é {imc:.2f}.\n{nome} nasceu em {ano}.')
