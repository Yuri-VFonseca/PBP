import random
elementos = []
num_elementos = random.randint(5,20)
for i in range(num_elementos + 1): 
    elementos.append(random.randint(1,10))
print(elementos)
print(sum(elementos))
print(sum(elementos)/len(elementos))