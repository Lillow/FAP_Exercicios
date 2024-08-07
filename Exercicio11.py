'''Ler x números, onde x é definido pelo usuário 
(o usuário que decide quando acaba).
Escreva o resultado da subtração entre as somas dos números pares e ímpares. 
Ex: soma dos pares - soma dos ímpares.'''

def coletar_valores() -> list:
    numeros = []
    while(True):
        entrada = input('Digite um número inteiro ou qualquer outra coisa para parar: ')
        try:
            n = int(entrada)
            numeros.append(n)
        except:
            print("Entrada não é um número. Parando a coleta de números.")
            break
    return numeros

def calcular_lista(valores: list) -> int:
    somaPar = 0
    somaImpar = 0
    for valor in valores:
        if valor % 2 == 0:
            somaPar += valor
        else:
            somaImpar += valor
    return somaPar - somaImpar

numeros = coletar_valores()
print(f'A subtração da soma dos pares e impares é {calcular_lista(numeros)}')