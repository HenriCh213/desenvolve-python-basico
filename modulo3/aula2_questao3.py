idade = int(input("Qual sua idade?"))
jogos = bool(input("Já jogou pelo menos 3 jogos de tabuleiros?"))
venceu = int(input("Quantos jogos já venceu?"))

if 16 < idade < 18:
    if jogos:
        if venceu >= 1:
            print("Apto para ingressar no clube de jogos de tabuleiros: True")
        else:
            print(False)
    else:
        print(False)
else:
    print(False)