genero = input("Qual o seu gênero? ").strip().lower()
mulher = ['mulher', 'woman', 'feminino', 'f']
homem = ['homem', 'man', 'masculino', 'm']
if genero not in mulher and genero not in homem: 
    print("Escreva o gênero correto")
else: 
    idade = int(input("Qual a sua idade? "))
    servico = int(input("Há quanto tempo você trabalha? "))
if genero in mulher: 
    aposentadoria = (idade > 60) or (servico >= 30) or (idade == 60) and (servico >= 25),
elif genero in homem: 
    aposentadoria = (idade > 65) or (servico >= 30) or (idade == 60) and (servico >= 25)
print(f"Aposentadoria liberada? {aposentadoria}")