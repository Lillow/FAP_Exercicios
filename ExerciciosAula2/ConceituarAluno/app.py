'''Vamos retomar o algoritmo de cálculo de media do aluno, 
e agora informar além da sua media qual o seu conceito:

media < 5,0 – Conceito: RUIM;
media >= 5,0 e media < 7,0 – Conceito: REGULAR;
media >= 7,0 e media < 8,0 – Conceito: BOM;
media >= 8,0 e media < 9,5 – Conceito: ÓTIMO;
media >= 9,5 – Conceito: EXCELENTE;
'''

class Aluno:
    def __init__(self, media):
        self.conceito: str
        self._conceituarAluno(media)


    def _conceituarAluno(self, media):
        if(media < 5.0):
            self.conceito =  'RUIM'
        elif(media >= 5.0 and media < 7.0):
            self.conceito =  'REGULAR'
        elif(media >= 7.0 and media < 8.0 ):
            self.conceito =  'BOM'
        elif(media >= 8.0 and media < 9.5 ):
            self.conceito =  'ÓTIMO'
        elif(media >= 9.5 ):
            self.conceito =  'EXCELENTE'   



media = float(input('Digite a média do aluno: '))
aluno = Aluno(media)


print('O conceito do aluno é %s'% aluno.conceito)