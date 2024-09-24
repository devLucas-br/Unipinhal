# Apresentar meses do ano em uma lista
print("Exercício 2")

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

num = int(input("Digite um número inteiro de 1 à 12: "))
print("Mês do Ano Respectivo: {}".format(meses[num-1]))