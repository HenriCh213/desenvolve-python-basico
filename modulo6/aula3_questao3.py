import random


for _ in range(20):
    lista = random.randint(-10, 10) 

print(f"Original: {lista}")

maior_qtd_negativos = 0
indice_intervalo = -1 
for i in range(len(lista) - 2):
    qtd_negativos = sum(1 for num in lista[i:i+3] if num < 0)
    if qtd_negativos > maior_qtd_negativos:
        maior_qtd_negativos = qtd_negativos
        indice_intervalo = i

if indice_intervalo != -1:
    del lista[indice_intervalo:indice_intervalo+3] 

print(f"Editada: {lista}")
    
