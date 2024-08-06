'''Ler as idades de 2 homens e de 2 mulheres 
(considere que as idades dos homens serão sempre diferentes entre si, 
bem como as das mulheres). 
Calcule e escreva a soma das idades do
homem mais velho com a mulher mais nova, 
e o produto das idades do homem mais novo com
a mulher mais velha.'''

def calcularIdades(homens: list, mulheres: list) -> list:
    maisVelho = homens[0]
    maisNovo = homens[0]
    for i in range(len(homens)):
        if i > maisVelho: maisVelho = homens[i]
        if i < maisNovo: maisNovo = homens[i]

    maisVelha = mulheres[0]
    maisNova = mulheres[0]
    for i in range(len(mulheres)):
        if i > maisVelha: maisVelha = mulheres[i]
        if i < maisNova: maisNova = mulheres[i]

    return [maisVelho + maisNova, maisNovo * maisVelha]

homens = [43, 12]
mulheres =[23, 41]
resultado =  calcularIdades(homens, mulheres)
print(f"A soma das idades é {resultado[0]} e o produto é {resultado[1]}")