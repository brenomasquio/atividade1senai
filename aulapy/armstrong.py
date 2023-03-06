print("Bem-vindo ao programa de verificação de números de Armstrong!")
num = int(input("Digite um número inteiro: "))

# convert o número em uma string para poder iterar pelos dígitos
num_str = str(num)

# inicializa a variável para armazenar a soma dos cubos dos dígitos
soma = 0

# itera pelos dígitos do número e adiciona o cubo de cada um à soma
for digito in num_str:
    soma += int(digito) ** 3

# verifica se a soma dos cubos dos dígitos é igual ao número original
if soma == num:
    print(num, "é um número de Armstrong!")
else:
    print(num, "não é um número de Armstrong.")
