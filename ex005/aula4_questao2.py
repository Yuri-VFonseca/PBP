#entrada de dados
f = int(input("Qual o valor da temperatura em  graus Fahrenheit? "))
#formulas
c = (f-32) * (5/9)
#saida de dados
print(f"{f} graus Fahrenheit são {c:.2f} graus Celsius")