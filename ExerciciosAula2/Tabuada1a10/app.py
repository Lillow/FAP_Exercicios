
'''
Por fim, iremos elaborar juntos um algoritmo 
que irá pedir ao usuário um número de 1 a 10, 
e o algoritmo irá calcular e exibir a tabuada desse número.
'''

def getNumConsole():
    num = 0
    while(num < 1 or num > 10):
        num = int(input('Digite um número de 1 a 10: '))
    return num

def calcularTabuada(num):
    for i in range(1, 10+1):
        print(f'{i} x {num} = {i*num}')

print('''
▀█▀ ▄▀█ █▄▄ █░█ ▄▀█ █▀▄ ▄▀█
░█░ █▀█ █▄█ █▄█ █▀█ █▄▀ █▀█
      ''')

calcularTabuada(getNumConsole())