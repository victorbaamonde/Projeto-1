foods = []
prices = []
total = 0

while True:
    food = input("Digite a comida a ser comprada (s para sair): ")
    if food.lower() == "s":
        break
    else:
        price = float(input(f"Digite o preco de {food}: R$"))
        foods.append(food)
        prices.append(price)

print("---- Seu carrinho ----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Seu total é {total}")
