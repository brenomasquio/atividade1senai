print("Bem-vindo ao programa de cálculo de aumento de salário!")
nome = input("Digite o nome do funcionário: ")
salario_antigo = float(input("Digite o salário do funcionário: "))

if salario_antigo <= 1500.0:
    aumento = salario_antigo * 0.1
else:
    aumento = salario_antigo * 0.05

salario_novo = salario_antigo + aumento
diferenca = salario_novo - salario_antigo

print("O novo salário de", nome, "é R$", salario_novo)
print("O aumento foi de R$", aumento)
print("A diferença entre o salário antigo e o novo é de R$", diferenca)
