# Notas e conceitos
print("Exercício 3")

notas = [0]*5 # Lista com 5 elementos
conc = [""]*5 # Lista com 5 elementos
for i in range(len(notas)): # Estrutura de Repetição que vai até o tamanho da lista (len: length)
    notas[i] = float(input(f"Qual a nota do {i +1}° aluno? "))
    if notas[i] >= 9: # Verificações
        conc[i] = "A" # Armazena o conceito na mesma posiçao que a nota, dependendo do valor dela
    elif notas[i] >= 7 and notas[i] < 9:
        conc[i] = "B"
    elif notas[i] >= 5 and notas[i] < 7:
        conc[i] = "C"
    else:
        conc[i] = "D"
for i in range(len(notas)):
    print(f"{i+1}° Aluno\nNota: {notas[i]} - Conceito: {conc[i]}")