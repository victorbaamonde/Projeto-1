'''
Crie um programa que recebe um numero e imprime o fatorial daquele numero

Método dos 5Q's para montar um algoritmo
Analise criticamente o problema e descubra:
    (Tente explicar este problema para voce mesmo em voz alta e peça mais informacoes/investigue
    ate compreender completamente o problema)

1. Quais sao os dados de entrada necessarios?
    numero
2. O que devo fazer com estes dados?
    calcular o fatorial do numero informado
3. Quais as restricoes deste problema?
    nao pode ser negativo e tem que ser um numero inteiro
4. Qual é o resultado esperado?
    o fatorial do numero informado
5. Qual é a sequencia de passos a ser feita para chegar ao resultado esperado?
    receber o numero
    calcular o fatorial
    criticar se o valor é negativo ou inteiro
    imprimir o valor do fatorial

'''
numero = int(input('Digite o numero para receber seu fatorial: '))
if numero > 0:
    fatorial = 1
    for valor_atual in range(1,numero +1):
        fatorial = fatorial * valor_atual
    print(fatorial)