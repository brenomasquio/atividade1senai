print("Bem-vindo ao programa de operações matemáticas!")
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

print("Escolha a operação que deseja realizar:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite o número da operação desejada: "))

if opcao == 1:
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)
elif opcao == 2:
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)
elif opcao == 3:
    resultado = num1 * num2
    print("O resultado da multiplicação é:", resultado)
elif opcao == 4:
    if num2 == 0:
        print("Não é possível dividir por zero!")
    else:
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
else:
    print("Operação inválida! Por favor, escolha uma operação válida (1, 2, 3 ou 4).")
