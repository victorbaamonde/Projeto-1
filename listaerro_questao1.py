# Questao 1
def soma1(a, b):
    return a + b
resultado = soma1(5,7)
print(f"O resultado da soma é: {resultado}")

# Questao 2
def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    media_total = soma / len(notas)
    return media_total

notas_alunos = [8.5, 7.2, 9.0, 5.5]
media = calcular_media(notas_alunos)
print("A média é:", media)

# Questao 3
def contar_vogais(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    for letra in palavra:
        if letra.lower() in vogais:
            contador += 1
    return contador

texto = "Python é uma linguagem de programação"
total_vogais = contar_vogais(texto)
print("O total de vogais é:", total_vogais)

# Questao 4
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
numero = 5
print("O fatorial de", numero, "é:", fatorial(numero))

# Questao 5

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
    def calcular_area(self):
        return self.lado_a * self.lado_b
retangulo = Retangulo(4, 6)
area = retangulo.calcular_area()
print("A área do retângulo é:", area)

# Questao 6
def calcular_media_refatorada(notas2):
    return sum(notas2)/len(notas2)

notas_refatorada = [8.5, 7.2, 9.0, 5.5]
media_aluno = calcular_media_refatorada(notas_refatorada)
print("A média do aluno é:", media_aluno)

# Questao 7
def contar_vogais_refatorada(palavra):
    vogais = set('aeiou')
    return sum(1 for letra in palavra.lower() if letra in vogais)
texto = "Python é uma linguagem de programação pica"
total_vogais = contar_vogais_refatorada(texto)
print("O total de vogais é:", total_vogais)





