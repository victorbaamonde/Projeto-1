'''
Escreva um programa que, ao inciar gera um valor aleatorio de 1 a 10 e permite que o usuario
chute um numero ate que o valor aleatorio gerado no inicio seja acertado

o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatorio gerado no inicio

5Q's
1. Quais os dados?
    valor aleatorio
    chute do usuaurio
2. O que fazer com os dados
    gerar o valor aleatorio
    receber o valor do usuario
    comparar os valores
    imprimir na tela se esta certo ou errado
    imprimir se acertou
3. Quais as restricoes?
    maior ou igual a 1
    menor ou igual a 10
4. Qual resultado esperado?
    informar acerto
5. Sequencia de passos
    
'''
import random
valor_aleatorio = random.randint(1, 10)


acertou = False
while acertou == False:
    chute_do_usuario = int(input('Digite um numero de 1 a 10: '))
    if chute_do_usuario < valor_aleatorio:
        print('Errou! Chutou para baixo')
    elif chute_do_usuario > valor_aleatorio:
        print('Errou! Chutou para cima')
    elif chute_do_usuario == valor_aleatorio:
        acertou = True
        print('Acertou')
