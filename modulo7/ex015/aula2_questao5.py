'''Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. 
Dica: use a biblioteca random.

def embaralhar_palavras(frase):

    #### Escreva a função


# Exemplo de uso:

frase = "Python é uma linguagem de programação"

resultado = embaralhar_palavras(frase)

print(resultado)

# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"
 '''
import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    embaralhadas = []
    for palavra in palavras: 
        if len(palavra) > 3: 
            primeira = palavra[0]
            ultima = palavra[-1]
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = primeira + ''.join(meio) + ultima
        else: 
            palavra_embaralhada = palavra
        embaralhadas.append(palavra_embaralhada)
    return ' '.join(embaralhadas)  

alvo = input("Digite uma frase para ser embaralhada: ")
resultado = embaralhar_palavras(alvo)
print(resultado)
