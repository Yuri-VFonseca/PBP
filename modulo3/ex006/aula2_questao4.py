classe = input("Qual a classe do personagem? Guerreiro, mago ou arqueiro? ").strip().lower()
validas = ['guerreiro','mago','arqueiro']
if classe not in validas: 
    print("Escolha uma clsse valida")
else: 
    forca = int(input("Qual a força do seu personagem? "))
    magia = int(input("Qual a magia do seu personagem? "))
if classe == 'guerreiro': 
    averiguar = (forca >= 15) and (magia <= 10)
elif classe == 'mago': 
    averiguar = (forca <= 10) and (magia >= 15)
elif classe == 'arqueiro': 
    averiguar = (forca > 5 < magia) and (forca <= 15 >= magia)
print(f"Pontos de atributo consistentes com a classe escolhida: {averiguar}")