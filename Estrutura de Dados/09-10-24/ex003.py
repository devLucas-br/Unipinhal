import math 

area = float(input("Digite o tamanho da área a ser pintada em m²: ")) # Recebe o valor da área
qntd_latas = math.ceil(area / 170) # Calcula a qntd de latas e arredonda para cima caso necessário
preco = qntd_latas * 480 # Calcula o valor
# Imprime ao usuário os valores
print(f"Quantidade de latas de tinta a serem compradas: {qntd_latas}")
print(f"Preço total: R$ {preco:.2f}")
