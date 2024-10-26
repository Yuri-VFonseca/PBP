'''4) Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
Exemplo de interação via terminal (entradas em negrito):
Digite a quantidade de elementos da lista 1: 4
Digite os 4 elementos da lista 1:
1
2
3
4Digite a quantidade de elementos da lista 2: 6
Digite os 6 elementos da lista 2:
5
6
7
8
9
10Lista intercalada: 1 5 2 6 3 7 4 8 9 10'''
lista1 = []
lista2 = []
intercalada = []
tamanho = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {tamanho} da lista 1: ")
for i in range(tamanho): 
    lista1.append(int(input()))
tamanho = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {tamanho} da lista 2: ")
for i in range(tamanho): 
    lista2.append(int(input()))
menor = min(len(lista1), len(lista2))
for i in range(menor):
    intercalada.append(lista1[i])
    intercalada.append(lista2[i]) 
if len(lista1) > len(lista2): 
    intercalada.extend(lista1[menor:])
else: 
    intercalada.extend(lista2[menor:])
print(f"Lista intercalada: {intercalada}")