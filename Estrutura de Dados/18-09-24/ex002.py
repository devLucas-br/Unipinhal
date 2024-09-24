# Soma dos valores de uma lista com 5 elementos
print("Exercício 2")

lista = [0]*5 # Cria uma lista com cinco elementos
soma = 0 # Define uma variável com valor zero
for i in range(len(lista)): # Estrutura de Repetição (vai até o tamanho da lista: 5 elementos)
    num = int(input(f"Digite o {i + 1}° valor: ")) # Recebe os números
    lista[i] = num # Atribui a cada posição da lista o número digitado
    soma += num # Atribui a soma cada valor digitado
print(f"Lista Dos Números Digitados: {lista}\nSoma Dos Valores Digitados: {soma}")