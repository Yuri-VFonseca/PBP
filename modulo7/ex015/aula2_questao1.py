'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e
imprima a data com o nome do mês por extenso. Dica: usando listas você não precisa
fazer um "if" para cada mês.
Digite uma data de nascimento: 29/10/1973
Você nasceu em 29 de Outubro de 1973.'''
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
data = input("Digite uma data de nascimento no formato XX/XX/XXXX: ")
info = data.split("/")
print(info)
dia, alvo, ano = info[0], info[1], info[2]
mes = int(alvo) - 1
n_mes = meses[mes]
print(f"Você nasceu em {dia} de {n_mes} de {ano}")