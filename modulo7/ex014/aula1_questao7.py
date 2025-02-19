'''Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:

Chave de criptografia: gere um valor n aleatório entre 1 e 10

Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

chave_aleatoria = 5

nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']'''
import random

def encrypt(names):
    key = random.randint(1, 10)
    encrypted_names = []
    for name in names:
        encrypted_name = ''
        for char in name:
            ascii_code = ord(char)
            if 33 <= ascii_code <= 126:
                encrypted_char = chr((ascii_code + key - 33) % 94 + 33)
                encrypted_name += encrypted_char
            else:
                encrypted_name += char
        encrypted_names.append(encrypted_name)
    return encrypted_names, key
encrypted_names = []
key = None
names_list = []
while True: 
    word = input("Type the words that you want to encrypt. To stop the program, type 0: ")
    if word == "0": 
        if len(names_list) == 0: 
            print("Não há elementos em sua lista.")
            break 
        else: 
            encrypted_names, key = encrypt(names_list)
            print("Nomes: ", names_list)
            print("Chave aleatória: ", key)
            print("Encrypt: ", encrypted_names)
            break 
    else: 
        names_list.append(word)
