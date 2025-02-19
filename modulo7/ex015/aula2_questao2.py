'''Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".

Digite uma frase: O rato roeu a roupa do rei

Frase modificada: * r*t* r*** * r**p* d* r**'''
vogais = ['a','e','i','o','u']
letras = input("Digite uma frase: ")
frase = letras.lower()
for vogal in vogais: 
    frase = frase.replace(vogal,"*")
print(frase)