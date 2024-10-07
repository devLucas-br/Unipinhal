# Receber e apresentar candidatos
candidatos = [] # Lista vazia
nome = "" # Variável str para receber os nomes
print("Cadastro de Candidatos")
for i in range(3): # Estrutura de Repetição: Armazenar os nomes  fornecidos 
    nome = input(f"Digite o nome do {i+1}° candidato: ") # Comando de Entrada
    candidatos.append(nome) # Adiciona no final da lista o nome fornecido

# Receber voto de cada condominio
votos = [0]*3 # [0, 0, 0]
voto = 0 # Variável int para receber cada voto
print("\nVotações")
print("Candidatos:")
for index, items in enumerate(candidatos): # Estrutura de Repetição: Apresentar cada cadidato com seu índice
    print(f"{items} - {index+1}")
for i in range(10): # Estrutura de Repetição: Receber os votos dos 10 condomínios
    while True: # Estrutra de Repetição: Verificar se o usuário digitou um número entre 1 e 3
        voto = int(input("Escolha seu candidato: ")) # Recebe o voto em int
        if voto in [1, 2, 3]: # Verificação
            votos[voto - 1] += 1 # Adiciona na lista votos o voto do candidato selecionado
            # (voto - 1): a lista votos começa na posição ZER0 e vai até 2
            # nós apresentamos os candidatos com numeração entre 1 e 3
            break # Quebra o 'while' e inicia novamente o for
        else: # Se o voto não estiver entre 1 e 3 repete o while
            print("Insira um número válido! Entre 1 e 3")

# Nomear vencedor
index_venc = votos.index(max(votos)) # Encontra o maior elemento da lista votos
venc = candidatos[index_venc] # Nomeia o vencedor de acordo com o maior índice encontrado
votos.pop(index_venc) # Remove os votos do vencedor
candidatos.pop(index_venc) # Remove o vencedor

# Verificação de Empate: 10 condomínios irão votar, consequentemente, sempre terá um vencedor
# Porém, se o primeiro lugar obteve 4 votos, os outros dois podem ter empatado, cada um com 3 votos 
if votos[0] == votos[1]: # Verifica se houve empate entre os dois restantes
    votos = [0]*2 # Zera os votos dos dois candidatos
    print("\nHouve empate na decisão do suplente\nSegunda votação")
    print("Candidatos:")
    # Mesma estrutura utilizada acima para receber votos
    for index, item in enumerate(candidatos):
        print(item, "-", index + 1)
    for i in range(10):
        while True:
            voto = int(input("Escolha seu candidato: "))
            if voto in [1, 2]:
                votos[voto - 1] += 1
                break
            else:
                print("Insira um número válido! Entre 1 e 2")
    index_sup = votos.index(max(votos)) # Nomeia o suplente de acordo com a segunda votação
    sup = candidatos[index_sup]
else: # Se não houve empate...
    sup = candidatos[votos.index(max(votos))] # Nomeia o suplente de acordo com a primeira votação

print(f"\nO vencedor da votação foi {venc}, seu suplente é {sup}")