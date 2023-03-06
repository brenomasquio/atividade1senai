print("Bem-vindo ao programa de classificação de idade!")
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade < 18:
    print(nome + ", você é menor de idade.")
elif idade >= 18 and idade <= 65:
    print(nome + ", você é adulto.")
else:
    print(nome + ", você é idoso.")
