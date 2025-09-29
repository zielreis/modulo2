#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete 
# com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega
#  em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor 
# do frete de acordo com as seguintes regras:

#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

#solicide a distancia mais o kg

# Solicita os dados do usuário
distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

# Define o preço por kg de acordo com a distância
if distancia <= 100:
    preco_por_kg = 1.0
elif distancia <= 300:
    preco_por_kg = 1.5
else:
    preco_por_kg = 2.0

# Calcula o valor base
valor_frete = peso * preco_por_kg

# Aplica a taxa extra para pacotes acima de 10 kg
if peso > 10:
    valor_frete += 10

# Exibe o resultado
print(f"Valor do frete: R${valor_frete:.2f}")