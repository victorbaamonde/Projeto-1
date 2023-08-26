peso = float(input("Digite seu peso: "))
unidade_peso = input("Quer em kg ou lbs? ")

if unidade_peso == "kg":
    print(f"Seu peso em kgs é {round(peso,2)}")
elif unidade_peso == "lbs":
    print(f"Seu peso em lbs é {round(peso*1.6,2)}")
else:
    print("Unidade de medida invalida")