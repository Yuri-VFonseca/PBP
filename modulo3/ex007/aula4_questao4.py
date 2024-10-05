 #Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg
distancia = int(input("Qual a distância em km da entrega? "))
peso = int(input("Qual o peso do pacote em kg? "))
taxa = 0
if peso > 10: 
    taxa = 10

if distancia <= 100: 
    valor = peso * 1 + taxa
elif (distancia >= 101 and distancia <= 300): 
    valor = peso * 1.5 + taxa
elif distancia > 300: 
    valor = peso * 2 + taxa
else: 
    print("Error")

print(f"O valor do frete é: R${valor}")