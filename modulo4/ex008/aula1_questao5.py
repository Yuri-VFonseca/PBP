respondentes = int(input("Qual o tamanho da amostra? ")) 
cont = 0
soma = 0
while cont < respondentes: 
    idades = int(input("Qual a sua idade? "))
    soma += idades
    cont += 1
media = idades / respondentes
print(f"A média da amostra é {media}")