'''Ler 3 valores e não aceitar valores menores que 1. 
Caso o usuário digite valor menor que 1,
repetir até obter todos os números. 
Escreva o resultado da soma dos números.'''

def pegarValores() -> list:
    valores = []
    while len(valores) < 3:
        valor = int(input('Digite um valor: '))
        if(valor >= 1):
            valores.append(valor)
    return valores

valores = pegarValores()
soma_total = sum(valores)

print(soma_total)