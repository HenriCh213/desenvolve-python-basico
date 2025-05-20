# É necessário 3 inputs para a resolução do exercício. Sendo eles: Comprimento, largura e preço
comprimento = float(input("Qual o comprimento?\n"))
largura = float(input("Qual a largura?\n"))
preco = float(input("Qual o preço?\n"))

# A variável 'área' irá armazena o valor da multiplicação entre 'comprimento' e 'largura'
area = float(comprimento * largura)

# A variável 'preco_total' irá armazena o valor da multiplicação entre 'area' e 'preco' == por conta do preço do terreno ser por área
preco_total = float(area * preco)


# Por fim, imprimimos a área 
print(f"O terreno possui {area}m² e custa R${preco_total}")
