import random, math

numeros = []

quantidade = random.randint(0, 10)
for n in range(quantidade):
    numeros.append(random.randint(0, 100))

soma = sum(numeros)
print(round(math.sqrt(soma), 2))