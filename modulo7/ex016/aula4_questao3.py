'''Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt". Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 

O texto das primeiras 25 linhas

O número de linhas do arquivo

A linha com maior número de caracteres

O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).'''
import re
with open("estomago.txt", "r", encoding="utf-8") as file: 
    lines = file.readlines()
    print("The first 25 lines of the file:")
    for i in range(min(25, len(lines))): 
        print(lines[i].strip())
    number_lines = len(lines)
    print(f"\nThe file has {number_lines} of lines.")
    long_line = max(lines, key=len)
    print(f"\nThe line with the most characters has: {len(long_line.strip())} characters")
    print(f"Line: {long_line.strip()}")
    text = ''.join(lines).lower()
    nonato_count = len(re.findall(r'\bnonato\b', text))
    iria_count = len(re.findall(r'\bíria\b', text))
    print(f"\nThe name 'Nonato is mentioned {nonato_count} times.")
    print(f"\nThe name Íria is mentioned {iria_count} times.")