# Laços de repetiçao + Listas
print('Carregando...')
print('Carregando...')
print('Carregando...')
print()

# O mesmo efeito acima pode ser feito com um laco de repeticao
for palavra in range(1, 4):
    print('Carregando...')
print()

for item in range(1,21):
    print(item)
print()

for item in range(1,21,2):
    print(item)
print()

nomes = ['victor','lorraine','bruna','elisa']
for nome in nomes:
    print(nome)
print()

# imprima os valores de 1 a N

valor_maximo = int(input('Digite o valor maximo: '))
valor_inicial = 1
for numero in range(valor_inicial,valor_maximo + 1):
    print(numero)
print()
