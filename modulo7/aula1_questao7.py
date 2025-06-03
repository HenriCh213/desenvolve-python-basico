import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    
    nomes_criptografados = []  
    
   
    for nome in nomes:
        nome_criptografado = ""
        
        for caractere in nome:
            novo_caractere = ord(caractere) + chave 
            if novo_caractere > 126: 
                novo_caractere = 33 + (novo_caractere - 127)
            nome_criptografado += chr(novo_caractere)
        
        nomes_criptografados.append(nome_criptografado)
    
    return nomes_criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)


print(f"Chave de criptografia: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_cript}")