# Solicita as idades
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris    = int(input("Digite a idade de Cris: "))

# Verifica se ambas são maiores de 17
pode_entrar = (idade_juliana > 17) and (idade_cris > 17)

# Imprime True ou False seguido de uma quebra de linha
if pode_entrar:
    print("True")
else:
    print("False")
