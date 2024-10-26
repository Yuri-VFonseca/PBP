import random
n = []
for i in range(20):
    n.append(random.randint(-100,100))

print(sorted(n))
print(n)
print(max(n))
print(min(n))
