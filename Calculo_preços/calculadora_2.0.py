# Calculadora feita para calcular o preço de venda de vários produtos
# Produtos possuem preço de custo diferentes mas as mesmas porcentagens de impostos incidem sobre eles
impostos = []
cadastro = ''
while cadastro != 'n' and cadastro != 'N':  # Loop permite o cadastro de uma quantidade infinita de impostos
    impostos += [float(input('Digite uma porcentagem de imposto: '))]
    cadastro = input('Deseja cadastrar novo imposto? (S) ou (N)')
lucro = float(input('Digite sua margem de lucro: '))  # Além dos impostos uma margem de lucro incide sobre o valor
custo = ''
contador = 0
while contador >= 0:
    custo = input('Digite o peço de custo, ou "sair": ')
    if custo == 'sair' or custo == 'Sair' or custo == 'SAIR':
        break
    total = float(custo)
    soma = float(custo)
    for contador in range(len(impostos)):
        total += soma * (impostos[contador] / 100)
        contador += 1
# Nessa versão as porcentagens dos impostos não estão sendo somados e sim aplicadas separadamente ao total
    total += total * (lucro / 100)  # Porcentagem de lucro aplicada separadamente após a aplicação dos impostos
    print(f'Preço de venda R${total:.2f}')
