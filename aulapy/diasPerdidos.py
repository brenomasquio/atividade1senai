print("Bem-vindo ao programa de cálculo de dias de vida perdidos devido ao fumo!")
idade = int(input("Digite a idade da pessoa: "))
cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))

# calcula o total de minutos perdidos por cigarro
minutos_por_cigarro = 10

# calcula o total de cigarros fumados pela pessoa até a idade atual
total_cigarros = cigarros_por_dia * (idade * 365)

# calcula o total de minutos perdidos devido ao hábito de fumar
total_minutos_perdidos = total_cigarros * minutos_por_cigarro

# converte o total de minutos perdidos em dias perdidos
dias_perdidos = total_minutos_perdidos / (24 * 60)

print("A pessoa perdeu", dias_perdidos, "dias de vida devido ao hábito de fumar.")
