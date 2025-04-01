data = input("Digite uma data de nascimento: ")
dat = data.split("/")
datar = []
for n in dat:
    datar.append(int(n))

mes = ["Inválido", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

print(f"Você nasceu em {datar[0]} de {mes[datar[1]]} de {datar[2]}.")
