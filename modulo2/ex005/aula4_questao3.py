#entradas
nome1 = input("Nome do produto 1 ")
preco1 = float(input(f"Qual o preço de {nome1}? "))
quantidade1 = int(input(f"Qual a quantidade comprada do {nome1}? "))
nome2 = input("Nome do produto 2 ")
preco2 = float(input(f"Qual o preço de {nome2}? "))
quantidade2 = int(input(f"Qual a quantidade comprada do {nome2}? "))
nome3 = input("Nome do produto 3 ")
preco3 = float(input(f"Qual o preço de {nome3}? "))
quantidade3 = int(input(f"Qual a quantidade comprada do {nome3}? "))
#formula
total = (preco1 * quantidade1) + (preco2 * quantidade2) + (preco3 * quantidade3)
#saida
print(f"Total: R${total:,.2f}")