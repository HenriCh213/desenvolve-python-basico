respondentes = int(input("Qual a quantidade de respondente?\n"))
respondente = respondentes

soma_idades = 0
while respondente != 0:
    n = int(input("Qual sua idade?\n"))
    soma_idades += n
    respondente -= 1

print((soma_idades)/respondentes)

