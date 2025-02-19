'''Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".

Digite uma frase (digite "fim" para encerrar): Radar

"Radar" é palíndromo

Digite uma frase (digite "fim" para encerrar): Bom dia!

"Bom dia!" não é palíndromo

Digite uma frase (digite "fim" para encerrar): Ame o poema

"Ame o poema" é palíndromo

Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!

"A Daniela ama a lei? Nada!" é palíndromo

Digite uma frase (digite "fim" para encerrar): fim'''
import string

while True: 
    entrada = input('Digite uma frase (digite "fim" para encerrar): ')
    entrada_lower = entrada.lower()
    if entrada_lower == "fim": 
        print("Até a próxima!")
        break
    palindromo = []
    frase = ''.join([char for char in entrada_lower if char not in string.punctuation])
    palindromo = frase[::-1]
    if frase == palindromo: 
        print(f"A frase {entrada} é um palíndromo")
    else: 
        print(f"A frase {entrada} não é um palíndromo")
           