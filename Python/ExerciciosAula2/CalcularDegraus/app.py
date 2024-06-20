'''Agora vamos elaborar um algoritmo que receba a altura do degrau de uma escada
e a altura que o usuário deseja alcançar subindo a escada. 
Calcular e mostrar quantos degraus o usuário deverá subir para atingir seu objetivo, 
sem se preocupar com a altura do usuário.'''

def calcDegraus(alturaDegrau, alturaDesejada):
    return int(alturaDesejada // alturaDegrau)

alturaDegrau = float(input('Digite a altura dos degraus: '))
alturaDesejada = float(input('Digite a altura que deseja alcançar: '))
numDegraus = calcDegraus(alturaDegrau, alturaDesejada)

print(f'Para subir {alturaDesejada} metros você precisará subir {numDegraus} degraus.')