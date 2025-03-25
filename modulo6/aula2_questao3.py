import random


lista1 = []
lista2 = []
interseccao = []
vezes = {}


for n in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

for n in lista1:
    if n in lista2 and n not in interseccao:
        interseccao.append(n)
        vezes1 = lista1.count(n)
        vezes2 = lista1.count(n)
        vezes[n] = (f"lista1={vezes1}", f"lista2={vezes2}")


print(lista1)
print(lista2)
interseccao.sort()
print(interseccao)

print("Contagem")
for n in interseccao:
    print(f"{n}: (lista1={lista1.count(n)}, lista2={lista1.count(n)})")