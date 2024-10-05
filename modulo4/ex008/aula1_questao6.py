totalcoelhos = 0
totalratos = 0
totalsapos = 0
cobaias = 0
cont = 0
experimentos = int(input("Qual a quantidade de experimentos realizados? "))

while cont < experimentos: 
    quantidade = int(input("Digite a quantidade de cobaias: "))
    cobaias += quantidade
    tipo = input("Digite o tipo de cobaia, s ou sapo, r ou rato, c ou coelho: ").lower().strip()
    
    sapo = ['sapo', 's', 'sapos']
    coelho = ['coelho', 'c', 'coelhos']
    rato = ['rato', 'r', 'ratos']
    
    if tipo in sapo: 
        totalsapos += quantidade
        print(f"Total de sapos: {totalsapos}")
        
    elif tipo in coelho: 
        totalcoelhos += quantidade
        print(f"Total de coelhos: {totalcoelhos}")
        
    elif tipo in rato: 
        totalratos += quantidade
        print(f"Total de ratos: {totalratos}")
        
    else:
        print("Tipo de cobaia inválido")
        cont -= 1  # Para não contar uma entrada inválida no loop
    
    cont += 1

# Cálculo das porcentagens
porcentagemsapo = (totalsapos / cobaias) * 100
porcentagemrato = (totalratos / cobaias) * 100
porcentagemcoelho = (totalcoelhos / cobaias) * 100

# Impressão dos resultados
print(f"Total de cobaias: {cobaias}")
print(f"Total de sapos: {totalsapos}")
print(f"Total de coelhos: {totalcoelhos}")
print(f"Total de ratos: {totalratos}")
print(f"Percentual de sapos: {porcentagemsapo:.2f}%")
print(f"Percentual de ratos: {porcentagemrato:.2f}%")
print(f"Percentual de coelhos: {porcentagemcoelho:.2f}%")
