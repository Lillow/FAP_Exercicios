'''Ler o salário fixo e o valor total das vendas efetuadas 
pelo vendedor de uma empresa.
Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas 
até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, 
calcular e escrever o seu salário total.'''

def calcularSalario(salarioFixo: float, valorTotVendas: float) -> float:
    comissao = valorTotVendas / 100 * 3
    if comissao > 1500:
        valorUltrapassado = (comissao - 1500) / 100 * 5
        comissao = 1500 + valorUltrapassado
    return salarioFixo + comissao

salarioFixo = float(input('Digite o salário fixo: R$ '))
valorTotVendas = float(input('Digite o valor total das vendas: R$ '))
salarioTotal = calcularSalario(salarioFixo, valorTotVendas)

print('O salário total é R$ %.2f'%salarioTotal)
