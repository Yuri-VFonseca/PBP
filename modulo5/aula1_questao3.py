import random
aleatorio = random.randint(1, 10)
while True: 
    n = int(input("Adivinhe o número entre 1 e 10: "))
    if n == aleatorio: 
        print(f"Correto! O número é {aleatorio}")
        break
    elif n > aleatorio: 
        print("Muito alto, tente novamente!")
    elif n < aleatorio: 
        print("Muito baixo, tente novamente!")
    else:
        print("ERROR")