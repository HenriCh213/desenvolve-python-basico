numero = input("Digite o número: ")

if len(numero) != 9:
    numero = f"9{numero}"

numero = numero[:5] + "-" + numero[5:]

print(numero)