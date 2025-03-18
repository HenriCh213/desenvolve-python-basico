n1 = int(input("Escolha um número:\n"))
n2 = int(input("Escolha um número:\n"))
n3 = int(input("Escolha um número:\n"))

m = (n1 + n2 + n3)/3

if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim")