numeros = []

while True:
    numero = input("Digite um número ou 'fim' para terminar o ciclo\n").lower()
    if numero == "fim" and len(numeros) >= 4:
        break
    elif numero == "fim":
        print("Digite pelo menos 4 números")
        print("\n" * 5)
        continue
    numeros.append(int(numero))    


print(numeros)
print(numeros[0:3])
print(numeros[-2:])
print(numeros[::-1])

numeros_even = []
numeros_odd = []
for n in numeros:
    if n % 2 == 0:
        numeros_even.append(n)
    else:
        numeros_odd.append(n)

print(numeros_even)
print(numeros_odd)