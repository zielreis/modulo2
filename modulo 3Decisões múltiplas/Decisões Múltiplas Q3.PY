#Você está desenvolvendo um sistema de avaliação de desempenho
# para um jogo. Escreva um programa em Python que avalia
# a pontuação do jogador em uma missão e atribui uma 
# classificação com base nas seguintes condições:

#Se a pontuação for menor que 70, atribua a classificação "Insatisfatório".
#Se a pontuação for maior ou igual a 70, atribua a classificação "Regular".
#Se a pontuação for maior ou igual a 80, atribua a classificação "Bom".
#Se a pontuação for maior ou igual a 90, atribua a classificação "Excelente".
#Escreva um programa que solicita ao usuário a pontuação e imprime a classificação correspondente.
 
 #pontuação dos jogos
 
pontuação = int (input("digite uma pontuação"))

# avaliação a classificação
if pontuação < 70:
    classificação = "insatisfatório"
    
elif pontuação >=90:
    classificação= "exelente"
    
elif pontuação >= 80:
    classificacao = "Bom"
else:  # de 70 até 79
    classificacao = "Regular"

# Exibe o resultado
print("Classificação:", classificacao)