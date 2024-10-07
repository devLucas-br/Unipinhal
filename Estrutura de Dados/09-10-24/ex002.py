produtos = [""]*8 # Cria uma lista vazia para receber os nomes
valores = [0]*8 # Cria uma lista vazia para receber os valores
for i in range(len(produtos)): # Estrutura de Repetição: Vai até o tamanho da lista
    produtos[i] = input(f"Insira o nome do {i+1}° produto: ") # Recebe o nome do produto
    valores[i] = float(input("Digite seu valor: ")) # Recebe o valor do produto
print("\nProdutos") 
for i in range(len(produtos)): # Estrutura de Repetição: Vai até o tamanho da lista
    print(f"{i+1} - {produtos[i]}: R$ {valores[i]:.2f}") # Apresenta cada produto cadastrado