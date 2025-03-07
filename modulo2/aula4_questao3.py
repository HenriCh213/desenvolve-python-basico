ordem = {}


produto1 = input("Digite o nome do produto 1:").title()
preco1 = float(input("Digite o preço unitário do produto 1:"))
quantidade1 = int(input("Digite a quantidade do produto 1:"))
ordem[produto1] = {'Preço':preco1, "Quantidade":quantidade1}

produto2 = input("Digite o nome do produto 2:").title()
preco2 = float(input("Digite o preço unitário do produto 2:"))
quantidade2 = int(input("Digite a quantidade do produto 2:"))
ordem[produto2] = {'Preço':preco2, "Quantidade":quantidade2}


produto3 = input("Digite o nome do produto 3:").title()
preco3 = float(input("Digite o preço unitário do produto 3:"))
quantidade3 = int(input("Digite a quantidade do produto 3:"))
ordem[produto3] = {'Preço':preco3, "Quantidade":quantidade3}


total = 0
for produto in ordem:
    preco = ordem[produto]['Preço']
    quantidade = ordem[produto]['Quantidade']
    preco_produto = float(preco * quantidade)
    total += preco_produto

print(f"Total R${total}")