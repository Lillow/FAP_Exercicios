'''1: Ler 4 valores (considere que não serão informados valores iguais). 
Escreva a soma dos dois últimos números.'''

def somaDoisUltimosNumeros(valores: list) -> int:
    return valores[-1] + valores[-2]

valores = []
for i in range(4): valores.insert(i, int(input(f'Digite o {i + 1}º: ') ))
print(somaDoisUltimosNumeros(valores))
