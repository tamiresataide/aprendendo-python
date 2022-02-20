# Versão 1.0 da calculadora para cálculo do preço de venda de um produto
# Produtos possuem preço de custo diferentes mas as mesmas porcentagens de impostos incidem sobre eles
impostos = []
cadastro = ''
while cadastro != 'n' and cadastro != 'N':
    impostos += [float(input('Digite uma porcentagem para calculo: '))]
    cadastro = input('Cadastrar nova porcentagem? (S) ou (N): ')
    while cadastro != 's' and cadastro != 'S' and cadastro != 'n' and cadastro != 'N':
        cadastro = input('Digite S ou N: ')
# Nessa versão o lucro está incluso junto das porcentagens dos impostos e não inserido separadamente
contador = 0
while contador >= 0:
    custo = input('Preço de custo ou "sair": ')
    if custo == 'sair':
        break
    total = float(custo)
    for contador in range(len(impostos)):
        total = total + (total * (impostos[contador] / 100))
        contador += 1
    print(f'Preço de venda R${total:.2f}')
# Nessa versão as porcentagens estão sendo somadas e aplicadas ao valor total resultando em um valor diferente
# Os impostos devem incidir sobre o valor do produto individualmente, por isso foi feita a versão 2.0
