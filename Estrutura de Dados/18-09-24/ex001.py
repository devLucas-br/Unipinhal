# Ordenar os valores de uma lista em ordem decrescente
print("Exercício 1")

lista = [] # Define uma lista vazia
maoir = meio = menor = 0 # Cria três variáveis com valor zero
num = 0 # Cria uma variável para receber os valores
for i in range(3): # Estrutura de Repetição 
    num = int(input("Digite um número: ")) # Recebe os valores
    lista.append(num) # Adiciona os valores na lista (.append)
lista.sort(reverse=True) # Ordena os valores da lista (reverse=True: decrescente)
print(lista)