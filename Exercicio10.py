'''Sistema de ordenação de valores. 
Ler 5 valores (considere que não serão informados valores iguais). 
Escrever os números em ordem DECRESCENTE.'''

valores = [int(input(f'{i + 1}º valor: ')) for i in range(5)]
valores.sort(reverse=True) # Ordena a lista de maneira decrescente
# valores.reverse() # Reverter a lista
# valores_invertidos = list(reversed(valores)) # A função reversed() retorna um iterador que pode ser convertido de volta para uma lista usando a função list().
# valores_invertidos = valores[::-1] # Usando o fatiamento para criar uma nova lista invertida.
print(valores)