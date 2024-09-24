# Verificador de números primos
print("Exercício 4")

numeros = [] # Lista vazia
primos = [] # Lista vazia
cont = 0 
num = 0

def primo(num): # Função que retorna True ou False / verifica se o número é oou não primo
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)
    if primo(num): # Utiliza a função criada para verificação
        primos.append(num)
        cont += 1

print(f"Quantidade de Números Primos digitada: {cont}\nPrimos: {primos}")