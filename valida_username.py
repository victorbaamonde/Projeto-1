# Valida um input de nome de usuario
# 1. Nao pode ter mais 12 caracteres
# 2. nao pode ter espacos
# 3. nao pode ter numeros


username = input("Digite um nome de usuario: ")

if len(username) > 12:
    print("Nao pode ter mais que 12 chars!")
elif not username.find(" ") == -1:
    print("Nao pode ter espacos!")
elif not username.isalpha():
    print("Nao pode ter digito")
else:
    print("Nome valido")