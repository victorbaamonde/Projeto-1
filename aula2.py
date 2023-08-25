# Condicionais
# if, elif e else
'''
E ae Victor, bora dar uma saida hoje?
Se eu terminar meu trabalho aqui, eu consigo
'''
trabalho_terminado = False
if trabalho_terminado == True:
    print('Opa! bora dar uma saida')
else:
    print('Nao consigo sair agora')

'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa nao for sua terceira vez chegando atrasado, entao pode sim, caso contrario ira tomar uma suspensao
'''

numero_de_atrasos = input('Digite o numero de atrasos')
if int(numero_de_atrasos) >= 3:
    print('Voce está suspenso')
    print()
elif numero_de_atrasos == 1:
    print('Pode entrar, porem caso tome mais duas faltas ira ser suspenso')
    print()
elif numero_de_atrasos == 2:
    print('Pode entrar, porem caso tome mais uma falta ira ser suspenso')
    print()
else:
    print('Pode entrar')
    print()

'''
Encontre o maior entre 2 numeros
'''

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')
if int(primeiro_valor) > int(segundo_valor):
    print('O primeiro valor é maior')
    print()
else:
    print('O segundo valor é maior')
    print()
