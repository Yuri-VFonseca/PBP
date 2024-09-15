#2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.
cris = int(input("Qual a idade de Cris? "))
juliana = int(input("Qual a idade de Juliana? "))
if cris > 17 or juliana > 17: 
    print("Sejam bem-vindos ao bar")
else: 
    print("Vocês não podem entrar")