'''Ler um valor numérico e escrever o seu antecessor. 
Ex: Ler n = 20, Escreva 19.'''

def mostrarAntecessor(numero: int) -> int:
    return numero -1

while(True):
    n = int(input('Digite um número ou -1 para sair: '))
    if(n < 0):
        break
    else:
        print(mostrarAntecessor(n))