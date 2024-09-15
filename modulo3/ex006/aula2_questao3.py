idade = int(input("Qual a sua idade? "))
jogos = input("Já jogou 3 jogos? Responda com true ou false: ").strip().lower() == 'true'
vitorias = int(input("Quantos jogos venceu? "))
apto = (16 <= idade <= 18) and jogos and (vitorias >= 1)
print(f"Apto para ingressar no clube? {apto}")