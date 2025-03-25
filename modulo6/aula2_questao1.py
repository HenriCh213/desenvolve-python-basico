import random

valores_aleatorios = []
ordem = []

for n in range(20):
    valores = random.randint(-100, 100)
    valores_aleatorios.append(valores)
    ordem.append(valores)

ordem.sort()
print(ordem)
print(valores_aleatorios)
print(max(valores_aleatorios))
print(min(valores_aleatorios))
