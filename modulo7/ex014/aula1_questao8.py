def validar_cpf(cpf):
    # Remover caracteres não numéricos
    cpf = cpf.replace('.', '').replace('-', '')  # Remover pontos e traços

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    # Verificar se o CPF é uma sequência de números iguais (ex: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return "Inválido"
    
    # Calcular o primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10) % 11
    if digito1 == 10:
        digito1 = 0

    # Calcular o segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10) % 11
    if digito2 == 10:
        digito2 = 0

    # Verificar se os dígitos calculados são iguais aos fornecidos
    if cpf[9] == str(digito1) and cpf[10] == str(digito2):
        return "Válido"
    else:
        return "Inválido"

# Solicitar CPF ao usuário
cpf_usuario = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

# Validar e exibir resultado
resultado = validar_cpf(cpf_usuario)
print(resultado)
