'''Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.
Digite seu nome: Fulano
F
Fu
Ful
Fula
Fulan
Fulano

'''
nome = input("Digite seu nome: ")
for i in range(1, len(nome), +1):
    print(nome[:i])