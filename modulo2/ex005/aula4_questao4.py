#entrada de dados
valor = int(input("Qual o valor? "))
#calculos
cem = valor // 100
nvalor = valor % 100
cinquenta = nvalor // 50
nvalor %= 50
vinte = nvalor // 20
nvalor %= 20
dez = nvalor // 10
nvalor %= 10
cinco = nvalor // 5
nvalor %= 5
dois = nvalor // 2
nvalor %= 2
um = nvalor // 1 
#saida
print(f"{cem} nota(s) de R$100,00")
print(f"{cinquenta} nota(s) de R$50,00")
print(f"{vinte} nota(s) de R$20,00")
print(f"{dez} nota(s) de R$10,00")
print(f"{cinco} nota(s) de R$5,00")
print(f"{dois} nota(s) de R$2,00")
print(f"{um} nota(s) de R$1,00")