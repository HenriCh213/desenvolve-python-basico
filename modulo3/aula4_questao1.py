numeros = []

for n in range(2):
    num = int(input("Informe um número:"))
    numeros.append(num)

if sum(numeros) % 2 == 0:
    print("Par")
else:
    print("Ímpar")