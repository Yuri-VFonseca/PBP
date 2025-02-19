'''Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
Digite o número: 97651234
Número completo: 99765-1234
Digite o número: 980876543
Número completo: 98087-6543 

'''
n = input("Digite o número: ")
if n.isdigit: 
    if len(n) == 8: 
        n ="9" + n
        n = n[:5] + "-" + n[5:]
        print("Número completo: " + n)
    if len(n) == 9: 
        n = n[:5] + "-" + n[5:]
        print("Número completo: " + n)
else: 
    print("Digite apenas números")