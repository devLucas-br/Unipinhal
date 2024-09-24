# Calcular e apresentar a tabuada de um número digitado pelo user
print("Exercício 3")

num = int(input("Digite o Número Que Deseja Calcular a Tabuada Aqui: ")) # Recebe o número para calcular a tab.
i = 1 # Inicia um contador em um
while i <= 10: # Estrutura de Repetição (de um até dez)
    print(f"{num} * {i} = {num * i}") # Apresenta cada multiplicação
    i += 1 # Soma um ao contador a cada repetição