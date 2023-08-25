'''
Levando em consideracao a velocidade maxima permitida de 80km em uma rua, crie um program que recebe do usuario
um valor de velocidade e diga se ele tomou uma multa leve, grave ou gravissima. Se estiver abaixo da permitida recebe
"nao houve multa", se estiver 10km acima, deve exibir: "multa leve", caso esteja entre 11 e 20km acima, exibir: "multa grave"
, e caso acima de 20km, exibir "multa gravissima"

5Q's
1. Quais os dados?
    velocidade 
2. O que fazer com os dados
    receber a velocidade
    comparar com a permitida
    exibir mensagem do tipo de multa
3. Quais as restricoes?
    velocidade positiva e maior q 0
4. Qual resultado esperado?
    informar multa
5. Sequencia de passos
    
'''
velocidadeMaxima = 80
velocidade = int(input('Digite a velocidade: '))
if velocidade <= velocidadeMaxima:
    print('Nao há multa.')
elif (velocidade > velocidadeMaxima) and (velocidade <= (velocidadeMaxima+10)):
    print('Multa leve')
elif (velocidade > velocidadeMaxima+10) and (velocidade <= (velocidadeMaxima+20)):
    print('Multa grave')
elif velocidade > velocidadeMaxima+20:
    print('Multa gravissima')