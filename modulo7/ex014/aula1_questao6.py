'''Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.

Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores

Digite a palavra objetivo: amor

Anagramas: ["amor", "mora", "ramo", "Roma"] '''
frase = input("Digite uma frase: ")
anagrama = input("Digite a palavra objetivo: ")
lst_palavras = frase.lower().split(" ")
for palavra in lst_palavras: 
    if sorted(palavra) == anagrama:
        print(anagrama)

'''Tentei fazer de outra maneira mas não consegui, por isso vou apenas explicita-lo. Inves de usar o sorted tentei correr pela palavra objetivo inteiramente, e comparar string por string com todas as palavras, se houvesse todas as ocorrencias das letras na palavra, daria certo, mas não consegui fazer rodar'''