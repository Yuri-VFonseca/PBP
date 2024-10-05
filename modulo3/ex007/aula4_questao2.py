#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem correspondente à classificação do filme:
#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."

filme = input("Digite um filme para ser avalidado ")
nota = int(input(f"Dê uma nota de 1 a 5 para {filme}: "))
if nota == 1: 
    print("Ruim")
elif nota == 2: 
    print("Regular")
elif nota == 3: 
    print("Bom!")
elif nota == 4: 
    print("Muito bom!")
elif nota == 5: 
    print("Excelente!")
else: 
    print("Error")