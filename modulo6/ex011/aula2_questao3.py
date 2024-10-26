import random
from collections import Counter
lista1 = []
lista2 = []
interseccao = []
for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))
interseccao = sorted(set(lista1) & set(lista2))
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)
print("lista 1 - ", lista1)
print("lista 2 - ", lista2)
print("Intersecção - ", interseccao)
print("Contagem")
for n in interseccao: 
        print(f"{n}: (lista1={contagem_lista1[n]}, lista2={contagem_lista2[n]})")
