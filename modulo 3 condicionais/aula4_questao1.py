#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar.
#  Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar.
#  Lembre-se do operador do python % que retorna o resto de uma divisão. 


# Solicita dois números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Calcula a soma
soma = num1 + num2

# Verifica se a soma é par ou ímpar usando o operador %
if soma % 2 == 0:
    print(f"A soma ({soma}) é PAR.")
else:
    print(f"A soma ({soma}) é ÍMPAR.")