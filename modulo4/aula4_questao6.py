vezes_cobaia = int(input("Informe o número de cobaias: "))

quantidade_sapo = 0
quantidade_coelho = 0
quantidade_rato = 0

while vezes_cobaia != 0:
    quantidade = int(input("Informa a quantidade: "))
    tipo = str(input("Informe o tipo: Sapo, Coelho ou Coelho")).title()
    if tipo == "Sapo":
        quantidade_sapo += quantidade
    elif tipo == "Coelho":
        quantidade_coelho += quantidade
    elif tipo == "Rato":
        quantidade_rato += quantidade

total_cobaias = quantidade_coelho + quantidade_rato + quantidade_sapo
print(f"Total de cobaias: {total_cobaias}")
print(f"Total de sapos: {quantidade_sapo}")
print(f"Total de coelhos: {quantidade_coelho}")
print(f"Total de ratos: {quantidade_rato}")

percentual_sapo = (quantidade_sapo // total_cobaias) * 100
percentual_coelho = (quantidade_coelho // total_cobaias) * 100
percentual_rato = (quantidade_rato // total_cobaias) * 100

print(f"Percentual do sapo: {percentual_sapo}%")
print(f"Percentual do rato: {percentual_rato}%")
print(f"Percentual do coelho: {percentual_coelho}%")