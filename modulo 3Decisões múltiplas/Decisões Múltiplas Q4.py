# # Sistema de desconto em loja online
valor = float(input("Digite o valor total da compra: "))

# Definindo o desconto conforme as condições
if valor >= 100:
    desconto = 0.20
elif valor >= 50:
    desconto = 0.10
else:
    desconto = 0.0

# Calculando o valor final
valor_final = valor * (1 - desconto)

# Exibindo resultados formatados
print(f"Desconto aplicado: {desconto * 100:.1f}%")
print(f"Valor final com desconto: R${valor_final:.2f}")