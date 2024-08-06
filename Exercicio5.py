'''Ler 11 valores numéricos, 
somar os 10 primeiros e guardar em uma variável A e o décimo primeiro valor, 
guardar em uma variável B. 
Escreva os valores de A e B. 
A seguir (utilizando apenas atribuições entre variáveis) 
troque os seus conteúdos fazendo com que o valor que está
em A passe para B e vice-versa. 
Ao final, escreva os valores que ficaram armazenados nas variáveis.'''


def lerSomarTrocar() -> None:
    valores = [int(input(f'{i + 1}ª valor: ')) for i in range(11)]
    varA = 0
    for i in range(10):
        varA = varA + valores[i]
    varB = valores[-1]
    varC = varA
    varA = varB
    varB = varC
    varC = None
    print(f"VarA = {varA} \nVarB = {varB}")


lerSomarTrocar()
