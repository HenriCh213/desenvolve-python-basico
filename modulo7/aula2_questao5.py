import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []

    for palavra in palavras:
        if len(palavra) <= 3:  
            nova_frase.append(palavra)
        else:
            meio = list(palavra[1:-1]) 
            random.shuffle(meio)
            nova_palavra = palavra[0] + "".join(meio) + palavra[-1]
            nova_frase.append(nova_palavra)

    return " ".join(nova_frase)



frase = input("Digite uma frase: ")
print(embaralhar_palavras(frase))
