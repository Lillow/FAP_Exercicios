'''Ler três valores que representam a idade de uma pessoa, 
expressa em anos, meses e dias (data de nascimento). 
Escreva a idade dessa pessoa expressa apenas em dias. Considerar ano
com 365 dias e mês com 30 dias.'''
from datetime import date

def idadePessoa(dia: int, mes: int, ano: int):
    data_nascimento = date(ano, mes, dia)
    print(f"Data de nascimento: {data_nascimento.strftime('%d/%m/%Y')}")

    hoje = date.today()
    idade_anos = hoje.year - data_nascimento.year
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade_anos -= 1
    print(f"Idade em anos: {idade_anos}")

    idade_dias = (hoje - data_nascimento).days
    print(f"Idade em dias: {idade_dias}")

idadePessoa(int(input('Dia: ')), int(input('Mês: ')), int(input('Ano: ')))