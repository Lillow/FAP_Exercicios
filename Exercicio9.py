'''Sistema de ordenação de valores. 
Ler 5 valores (considere que não serão informados valores iguais). 
Escrever os números em ordem CRESCENTE.'''

valores = [int(input(f'{i + 1}º valor: ')) for i in range(5)]
valores.sort()
print(valores)