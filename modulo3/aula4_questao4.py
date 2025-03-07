distancia = int(input("Qual a distância?"))
peso = int(input("Qual o peso?"))


preco = 0
if distancia <= 100:
    preco = peso
elif distancia > 100 and distancia < 300:
    preco = peso * 1.5
elif distancia > 300:
    preco = peso * 2
if peso > 10:
    preco += 10
    
print(preco)