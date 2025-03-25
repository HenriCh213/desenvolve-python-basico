frase = input("Digite uma frase: ").lower()
espaco_frase = frase.replace(" ", "")


Vogais = []
Consoantes = []
if "a" in frase:
    a = frase.count("a")
    for n in range(a):
        Vogais.append("a")
if "e" in frase:
    e = frase.count("e")
    for n in range(e):
        Vogais.append("e")
if "i" in frase:
    i = frase.count("i")
    for n in range(i):
        Vogais.append("i")
if "o" in frase:
    o = frase.count("o")
    for n in range(o):
        Vogais.append("o")
if "u" in frase:         
    u = frase.count("u")
    for n in range(u):
        Vogais.append("u")

for n in espaco_frase:
    if n != "a" and n != "e" and n != "i" and n != "o" and n != "u":
        Consoantes.append(n)

print(f"Vogais: {Vogais}")
print(f"Consoantes: {Consoantes}")