'''1) Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
A lista original
Os 3 primeiros elementos
Os 2 últimos elementos
A lista invertida (do fim para o começo)
Os elementos de índice par (0, 2, 4 … )
Os elementos de índice ímpar (1, 3, 5, … )'''
lista = []
n = int(input("Qual vai ser o tamanho da lista (minimo 4 valores): "))
if n < 4: 
    print("O valor não pode ser menor que 4")
else: 
    print("Digite os valores para a lista")
    for i in range(n): 
        valores = int(input())
        lista.append(valores)
print("Lista: ", lista)
print("3 primeiros itens: ", lista[:3])
print("2 últimos itens: ", lista[-2:])
print("Lista invertida: ", lista[::-1])
print("Elementos índice par: ", lista[::2])
print("Elementos índice ímpar: ", lista[1::2])