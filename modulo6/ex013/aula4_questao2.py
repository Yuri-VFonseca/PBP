vogais = []
consoantes = []
permissao = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
frase = input("Digite uma frase: ")
vogais = sorted([letra for letra in frase if letra in permissao])
consoantes = [letra for letra in frase if letra.isalpha() and letra not in permissao]
print(vogais)
print(consoantes)