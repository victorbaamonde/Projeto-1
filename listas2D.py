fruits = ["banana", "orange", "pineapple"]
vegetables = ["carrot", "potato", "tomato"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0])
print()
print(groceries[0][2])
print()

for collection in groceries:
    for food in collection:
        print(food, end=" ")
print()
print()
# teclado numerico de telefone

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
