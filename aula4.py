# Coleçoes(listas)
preco_1 = 20
preco_2 = 50
preco_3 = 100
print()

# Codigo acima pode ser feito com listas. Colecoes possuem indices ou posicoes na lista
precos = [20, 50, 100]
# indices 0 , 1, 2
print(precos[1])  # imprime a posicao 1 da lista, o numero 50
# o index informa a posicao de um valor dentro de uma lista
print(precos.index(100))
print()

# Lista
diversidades = [15, 'victor', True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
print()

# Lista interavel

for preco in precos:
    print(preco)
print()
for diversidade in diversidades:
    print(diversidade)
print()

# Some os valores: dado uma colecao de dados 'idades' [15,20,25,35,40] imprima na tela a soma desses valores

idades = [15, 20, 25, 35, 40]
soma = 0
for idade in idades:
    soma = soma + idade
print(soma)
print()
