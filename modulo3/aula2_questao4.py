classe = input("Escolha a classe (guerreiro, mago ou arqueiro):").lower()
forca = int(input("Digite os pontos de força (de 1 a 20):"))
magia = int(input("Digite os pontos de magia (de 1 a 20):"))

if classe == "guerreiro":
    if forca >= 15 and magia <= 10:
        print(True)
    else:
        print(False)
if classe == "mago":
    if forca <= 10 and magia >= 15:
        print(True)
    else:
        print(False)
if classe == "arqueiro":
    if forca > 5 and magia > 5 and forca < 15 and magia < 15:
        print(True)
    else:
        print(False)