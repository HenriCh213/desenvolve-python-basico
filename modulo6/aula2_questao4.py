quantidade1 = int(input("Digite a quantidade de elementos da lista 1: "))

lista1 = [int(input(f"Digite os {quantidade1} elementos da lista 1: ")) for n in range(quantidade1)]

lista1.sort()
print(lista1)

quantidade2 = int(input("Digite a quantidade de elementos da lista 2: "))

lista2 = [int(input(f"Digite os {quantidade1} elementos da lista 2: ")) for n in range(quantidade2)]

lista2.sort()
print(lista2)

min1 = min(lista1)
min2 = min(lista2)
lista_intercalada = []

if quantidade1 > quantidade2:
    for n in lista1:
        if min1 < min2:
            lista_intercalada.append(lista1[n])
            lista1.remove(n)
        else:
            lista_intercalada.append(lista2[n])
            lista2.remove(n)

print(lista_intercalada)