genero = input("Fale seu gênero?").title()
idade = int(input("Qual sua idade?"))
servico = int(input("Tempo de serviço?"))

if genero == "F":
    if idade > 60 or servico >= 30 or idade == 60 and servico >= 25:
        print(True)
    else:
        print(False)
if genero == "M":
    if idade > 65 or servico >= 30 or idade == 60 and servico >= 25:
        print(True)
    else:
        print(False)