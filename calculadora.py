operador = input("Digite um operador (+,-,*,/): ")
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if operador == "+":
    result = num1 + num2
    print(f"O resultado da operação é {round(result,2)}")
elif operador == "-":
    result = num1 - num2
    print(f"O resultado da operação é {round(result,2)}")
elif operador == "*":
    result = num1 * num2
    print(f"O resultado da operação é {round(result,2)}")
elif operador == "/":
    result = num1 / num2
    print(f"O resultado da operação é {round(result,2)}")
else:
    print(f"Operador {operador} nao é valido")
    