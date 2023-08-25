# Variáveis

# Números
velocidade_internet = 10
print(velocidade_internet)
print()
nota_filme = 8.5 #float
# Valores booleanos
esta_aberto = True #or False
# Strings
nome_do_curso = 'Aspas simples' 
nome_do_curso2 = "Aspas duplas"

# Como variáveis podem ser usadas para a vida real?
# Problema 1 - Valor por hora de funcionario
# Escreva um programa que retorne o valor hora de um funcionario com base no seu salário mensal e horas trabalhadas

salario_mensal = input('Qual é o seu salário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas trabalha por mes')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)