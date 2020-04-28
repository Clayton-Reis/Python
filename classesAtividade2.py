# 1) Crie um programa para representar funcionários em um sistema de gestão de pessoas.

# É necessário que nesta modelagem seja feito uso de, no mínimo, duas classes ('FUNCIONÁRIOS' e 'SETORES'  uma associação entre estas).
# Cada classe deverá ter no mínimo 2 atributos.

class Funcionario:
    def __init__ (self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Setores(Funcionario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.secretaria = []

    def setEscritorio(self, funcionario):
        self.escritorio = funcionario

    def setSecretaria(self, funcionario):
        self.secretaria.append(funcionario)


setor1 = Setores("Escritório")
pessoa2 = Funcionario("Mateus",2574)
pessoa3 = Funcionario("Joana", 2575)

setor1.setEscritorio(pessoa2)
setor1.setSecretaria(pessoa3)

print ("Setor 1")
print (f'Setores: \n {setor1.nome}')
print (f'Funcionário: \n {pessoa2.funcionario}')
print (f'Secretaria: \n {pessoa3.secretaria}')

