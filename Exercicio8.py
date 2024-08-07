'''Ler o número total alunos de uma sala de aula, 
o número de votos em candidato A e candidato B. 
Escreva o percentual que cada candidato representa em relação ao total de alunos.
Considere que o número total de alunos votou no candidato A ou B'''


def calcular_porcentagem(total, votos):
    return (votos / total) * 100 if total > 0 else 0


def calcular_votos(total_votos: int, votos_A: int, votos_B: int):
    total_A = calcular_porcentagem(total_votos, votos_A)
    total_B = calcular_porcentagem(total_votos, votos_B)
    resto = calcular_porcentagem(
        total_votos, (total_votos - (votos_A + votos_B)))
    return total_A, total_B, resto

votos_txr = int(input('Digite o total de alunos: '))
votos_A = int(input("Digite o número de votos no candidato A: "))
votos_B = int(input("Digite o número de votos no candidato B: "))
votos_A, votos_B, votos_txr = calcular_votos(votos_txr, votos_A, votos_B)

print(f"Porcentagem dos votos no candidato A: {votos_A:.2f}%")
print(f"Porcentagem dos votos no candidato B: {votos_B:.2f}%")
print(f"Porcentagem dos alunos que não votaram nem no candidato A e nem no candidato B: {resto:.2f}%")
