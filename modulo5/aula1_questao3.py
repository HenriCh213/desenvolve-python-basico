from random import randint

numero = randint(0, 10)
while True:
    advinhe = int(input("Advinhe o número entre 1 e 10:"))
    if advinhe > numero:
        print("Muito alto, tente novamente!")
    elif advinhe < numero:
        print("Muito baixo, tente novamente!")
    else:
        print(f"Correto! O número é {numero}")
        break