vezes_cobaia = int(input("Informe o número de cobaias: "))

quantidade_sapo = 0
quantidade_coelho = 0
quantidade_rato = 0

while vezes_cobaia != 0:
    quantidade = int(input("Informa a quantidade: "))
    tipo = str(input("Informe o tipo: Sapo, Rato ou Coelho\n")).title()
    if tipo == "Sapo":
        quantidade_sapo += quantidade
    elif tipo == "Coelho":
        quantidade_coelho += quantidade
    elif tipo == "Rato":
        quantidade_rato += quantidade
    vezes_cobaia -= 1

total_cobaias = quantidade_coelho + quantidade_rato + quantidade_sapo
print(f"Total de cobaias: {total_cobaias}")
print(f"Total de sapos: {quantidade_sapo}")
print(f"Total de coelhos: {quantidade_coelho}")
print(f"Total de ratos: {quantidade_rato}")

percentual_sapo = round((quantidade_sapo / total_cobaias) * 100, 2)
percentual_coelho = round((quantidade_coelho / total_cobaias) * 100, 2)
percentual_rato = round((quantidade_rato / total_cobaias) * 100, 2)

print(f"Percentual do sapo: {percentual_sapo}%")
print(f"Percentual do rato: {percentual_rato}%")
print(f"Percentual do coelho: {percentual_coelho}%")
