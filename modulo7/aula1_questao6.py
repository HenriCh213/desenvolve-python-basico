def ordenar_palavra(palavra):
    return ''.join(sorted(palavra))

frase = input("Digite uma frase: ").lower()  
palavra_objetivo = input("Digite a palavra objetivo: ").lower()

palavra_ordenada = ordenar_palavra(palavra_objetivo)

anagramas = []

for palavra in frase.split():
    palavra_limpa = ''.join(letra for letra in palavra if letra.isalpha())
    
    if ordenar_palavra(palavra_limpa) == palavra_ordenada:
        anagramas.append(palavra)

print(f"Anagramas: {anagramas}")
