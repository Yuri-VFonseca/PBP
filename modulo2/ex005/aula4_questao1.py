#coleta de dados
preco_m2 = float(input("Qual o valor do metro quadrado? "))
comprimento = float(input("Qual o comprimento do terreno? "))
largura = float(input("Qual a largura do terreno? "))
#formulas
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2
#saida de dados
print(f"O terreno possui {area_m2:,.2f}m² e custa R${preco_total:,.2f}")
