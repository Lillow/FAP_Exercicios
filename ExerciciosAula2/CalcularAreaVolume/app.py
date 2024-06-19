'''Agora elaborem um algoritmo que peça ao usuário 
o valor do raio de uma esfera 
e calcule a área de sua superfície e o volume da esfera. 
Use Pi como uma constante com valor de 3,1415. A = 4πr² | V = (4/3)πr³
'''
class Esfera:

    def __init__(self, raio):
        import math
        pi = math.pi
        self.area = 4 * pi * (raio ** 2)
        self.volume = (4 / 3) * pi * (raio ** 3)


esfera = Esfera(float(input("Informe o valor do raio da esfera: "))) 

print("A área da superfície da esfera é: %.4f"% esfera.area)

print("O volume da esfera é: %.4f"% esfera.volume) 


