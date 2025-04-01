


frase = input("Digite uma frase (digite 'fim' para encerrar): ")
frase_lower = frase.lower()


for n in frase_lower:
    if n == " ":
        frase_lower = frase_lower.replace(" ", "")
    elif n == "!" or n == "?":
        frase_lower = frase_lower.replace(n, "")

inverso = frase_lower[::-1]

for n in inverso:
    if n == " ":
        inverso = inverso.replace(" ", "")
    elif n == "!" or n == "?":
        inverso = inverso.replace(n, "")

if inverso == frase_lower:
    print(f"'{frase}' é palíndromo.")
else:
    print(f"'{frase}' não é palíndromo.")

