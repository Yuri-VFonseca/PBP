import random
import math
n = int(input("Digite o valor de n: "))
soma = 0
for i in range(n):
    aleatorio = random.randint(1,100)
    soma += aleatorio
    print(aleatorio)
raiz = math.sqrt(soma)
print(f"Soma: {soma}")
print(f"Raiz quadrada: {raiz}")