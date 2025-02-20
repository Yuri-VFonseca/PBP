'''Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.

Digite uma frase: Bom dia, meu nome é Davi.

Frase salva em /Users/laranjeira/python-basico/frase.txt'''

import os, sys
frase = input("Digite uma frase: ")
arquivo = "frase.txt"
diretorio = os.path.abspath(os.path.dirname(__file__))
caminho = os.path.join(diretorio, arquivo)
with open(caminho, "w", encoding="utf-8") as arquivo: 
    arquivo.write(frase)
print(f"Frase salva em {caminho}")