caracteres = "!@#$%^&*()-+?_=,<>/"

def validador_senha(senha):
    if len(senha) < 8:
        return False

    maiscula = False
    minuscula = False
    numero = False
    caractere = False

    for n in senha:
        if n.isupper(): 
            maiscula = True
        elif n.islower():
            minuscula = True
        elif n.isdigit():
            numero = True
        elif n in caracteres:
            caractere = True
        
    return maiscula and minuscula and numero and caractere
        
senha = input("Digite a sua senha: ")



print(validador_senha(senha))