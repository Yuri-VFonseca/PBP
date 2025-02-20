'''Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".

Bom

dia

meu

nome

é

Davi'''
import os
with open("frase.txt", "r", encoding="utf-8") as arquivo: 
    conteudo = arquivo.read()
print(conteudo)
palavras = [palavra + "\n" for palavra in conteudo.split()]
with open("palavras.txt", "w", encoding="utf-8") as arquivo: 
    quebras = arquivo.writelines(palavras)
with open("palavras.txt", "r", encoding="utf-8") as arquivo: 
    print(arquivo.read())