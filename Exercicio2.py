'''Ler 2 valores e se o segundo valor informado for ZERO, 
deve ser lido um novo valor, ou seja,
para o segundo valor não pode ser aceito o valor zero 
,e imprimir o resultado da divisão do
primeiro valor lido pelo segundo valor lido. 
(utilizar a estrutura REPETIR)'''


def divisaoValores(num1: int, num2: int) -> float:
    return num1 / num2

num1 = int(input('Digite o primeiro valor: '))
num2 = 0
while(num2 == 0): num2 = int(input('Digite o segundo valor(diferente de 0): '))

print(f'Resultado: {divisaoValores(num1, num2)}')