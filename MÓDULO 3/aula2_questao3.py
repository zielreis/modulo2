#5 - Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) 
# e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário,
#  de acordo com as seguintes regras:
#A: Para mulheres, ter mais de 60 anos. Para homens, 65.

#B: Ou ter trabalhado pelo menos 30 anos

#C: Ou ter 60 anos  e trabalhado pelo menos 25

# Solicita os dados do usuário

genero = input("Informe seu gênero (M/F): ").upper()
idade = int(input("Informe sua idade: "))
tempo_servico = int(input("Informe seu tempo de serviço (em anos): "))

# Verifica as condições de aposentadoria
aposentadoria = (
    (genero == "F" and idade > 60) or   # Regra A: mulheres com mais de 60
    (genero == "M" and idade > 65) or   # Regra A: homens com mais de 65
    (tempo_servico >= 30) or            # Regra B: 30 anos de serviço
    (idade >= 60 and tempo_servico >= 25)  # Regra C: 60 anos e 25 de serviço
)

# Exibe o resultado
print(aposentadoria)
