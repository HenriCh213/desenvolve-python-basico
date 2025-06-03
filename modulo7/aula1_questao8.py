def calcular_primeiro_digito(cpf):
    cpf_numeros = [int(digito) for digito in cpf if digito.isdigit()]
    
    if len(cpf_numeros) < 9:
        return None 
    
    multiplicadores = list(range(10, 1, -1))
    
    soma = sum(cpf_numeros[i] * multiplicadores[i] for i in range(9))
    
    resto = soma % 11
    
    if resto < 2:
        return 0
    else:
        return 11 - resto

cpf = input("Digite um CPF no formato XXX.XXX.XXX-XX: ")

primeiro_digito_calculado = calcular_primeiro_digito(cpf)

if primeiro_digito_calculado is not None:
    primeiro_digito_informado = int(cpf[12])
    if primeiro_digito_calculado == primeiro_digito_informado:
        print("Primeiro dígito verificador é válido.")
    else:
        print("Primeiro dígito verificador é inválido.")
else:
    print("CPF inválido.")