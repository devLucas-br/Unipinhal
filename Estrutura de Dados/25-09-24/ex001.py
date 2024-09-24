# Definir categoria do nadador de acordo com idade
print("Exercício 1")

print("Avaliador de Categoria")
idade = int(input("Qual a idade do nadador? ")) # Comando de Entrada

if idade >= 5 and idade <= 7: # Aqui começam as verificações
    print("Nadador de Categoria: Infantil A")
elif idade >= 8 and idade <= 10:
    print("Nadador de Categoria: Infantil B")
elif idade >= 11 and idade <= 13:
    print("Nadador de Categoria: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Nadador de Categoria: Juvenil B")
else:
    print("Nadador de Categoria: Sênior")