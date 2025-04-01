frase = input("Digite uma frase: ").lower()
for n in frase:
    if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
        frase = frase.replace(n, "*")

print(frase)