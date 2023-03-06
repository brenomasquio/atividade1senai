print("Bem-vindo ao programa de soma de dígitos!")
numero = input("Digite um número inteiro de três dígitos: ")

if len(numero) != 3:
    print("Número inválido.")
else:
    digito1 = int(numero[0])
    digito2 = int(numero[1])
    digito3 = int(numero[2])
    soma = digito1 + digito2 + digito3
    print("A soma dos dígitos é:", soma)
