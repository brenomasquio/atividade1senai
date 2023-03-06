print("Bem-vindo ao programa de cálculo de média!")
numero1 = int(input("Digite a primeira nota: "))
numero2 = int(input("Digite a segunda nota: "))
numero3 = int(input("Digite a terceira nota: "))

media = (numero1 + numero2 + numero3) / 3

print("A média aritmética dos números é:", media)

if media >= 7:
    print("Aprovado!")
elif media >= 5 and media < 7:
    print("Recuperação.")
else:
    print("Reprovado.")
