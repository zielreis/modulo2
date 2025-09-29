#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários.
#  Escreva um programa em Python que solicita ao usuário para inserir a 
# avaliação de um filme em uma escala de 1 a 5. 
# O programa deve imprimir uma mensagem correspondente à classificação do filme:



# Solicita ao usuario a avaliação 

avaliacao=int(input("digite uma avaliação  mumero de 1a5" ))

# resposta do usuario
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Digite um número de 1 a 5.")

