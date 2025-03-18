n = int(input("Escolha um número:\n"))

maior = 0

while n > 0:
    x = int(input("Escolha um número:\n"))
    if x > maior:
        maior = x
    n -= 1

print(maior)