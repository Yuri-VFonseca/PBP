'''
Fazer CRUD -  Create, Read, Update and Delete
Usuários - Controle de acesso (usuario (ver itens), gerente (ver, criar, reduzir e aumentar n de itens e colocar novos preços) e funcionário (ver e reduzir ou aumentar n de itens)
Organizar em um doc (.csv)
Produtos ou serviços - armazernar em um .csv separado, aplicar crud
'''
import random
import csv
#funcoes - produtos
produtos = []
#create
def create_produto(produto): 
    with open('produtos.csv', 'a', newline='', encoding="UTF-8") as file: 
        writer = csv.writer(file)
        writer.writerow(produtos) # criar colunas na planilha 
def info_produtos(nome, preco, quantidade):
    codigo = random.randint(10000000, 999999999) # criar codigo aleatorio
    produtos = [nome, preco, quantidade, codigo]
    create_produto(produto)
#read
def buscar_produto(chave): 
    with open('produtos.csv', 'r', newline='') as file: 
        reader = csv.reader(file)
        next(reader, None)
        for linha in reader: 
            if len(linha) < 4: 
                continue
            nomeproduto, preco, quantidade, codigo = linha
            if nomeproduto == chave.lower() or codigo == chave: 
                return {"Nome": nomeproduto, "Preço": float(preco), "Quantidade": int(quantidade), "Código": int(codigo)} # chave - produto
            return None
#update
def update_produto(codigo, nome=None, preco=None, quantidade=None): 
    produtos_atualizados = []
    with open('produtos.csv', 'r', newline='', encoding="UTF-8") as file: 
        reader = csv.reader(file)
        next(reader, None)
        for linha in reader: 
            if linha and int(linha[3]) == codigo: 
                if nome: linha[0] = nome
                if preco: linha[1] = preco
                if quantidade: linha[2] = quantidade
            produtos_atualizados.append(linha)
    with open('produtos.csv', 'w', newline='', encoding="UTF-8") as file: 
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Preço', 'Quantidade', 'Código'])
        writer.writerow(produtos_atualizados)
#delete
def delete_produto(chave): 
    produtos_atualizados = []
    with open('produtos.csv', 'r', newline="", encoding="UTF-8") as file: 
        reader = csv.reader(file)
        next(reader, None)
        for linha in reader: 
            if linha: 
                nomeproduto, preco, quantidade, codigo = linha
                if nomeproduto == chave or int(codigo) == chave: 
                    continue 
            produtos_atualizados.append(linha)
    with open('produtos.csv', 'w', newline='', encoding="UTF-8") as file: 
        writer = csv.writer(file)
        writer.writerow(["Nome", "Preço", "Quantidade", "Código"])
        writer.writerows(produtos_atualizados)
    
    #usuarios
#create 
def create_usuario(usuario): 
    return 
#read

#update

#delete

#cliente (ver produto, alterar suas info)

#funcionario (ver, dar baixa e aumentar, atualizar clientes e criar)

#gerente (todo o restante + cadastrar novos produtos e alterar preços, CRUD clientes)

# Variaveis, listas e cabeçalho
with open("produtos.csv", 'w', newline="", encoding="UTF-8") as file: 
    writer = csv.writer(file)
    writer.writerow(["Nome", "Preço", "Quantidade", "Código"])


'''
produtos_lista = [
    ["Cerveja Skol 350ml", 3.99, 100],
    ["Cerveja Brahma 350ml", 4.29, 90],
    ["Cerveja Heineken 330ml", 6.99, 80],
    ["Cerveja Corona 330ml", 7.49, 75],
    ["Cerveja Budweiser 350ml", 5.99, 85],
    ["Cerveja Stella Artois 275ml", 6.49, 60],
    ["Cerveja Original 600ml", 9.99, 50],
    ["Cerveja Bohemia 600ml", 8.99, 55],
    ["Whisky Johnnie Walker Red Label 1L", 89.99, 20],
    ["Whisky Jack Daniels 1L", 129.99, 15],
    ["Vodka Smirnoff 1L", 39.99, 25],
    ["Vodka Absolut 1L", 99.99, 20],
    ["Gin Tanqueray 750ml", 119.99, 18],
    ["Gin Bombay Sapphire 750ml", 129.99, 12],
    ["Energético Red Bull 250ml", 9.99, 50],
    ["Energético Monster 473ml", 12.99, 40],
    ["Refrigerante Coca-Cola 2L", 8.99, 60],
    ["Refrigerante Guaraná Antarctica 2L", 7.99, 55],
    ["Refrigerante Sprite 2L", 8.49, 50],
    ["Suco de Laranja Natural 1L", 12.99, 30],
    ["Água Tônica Schweppes 350ml", 5.99, 40],
    ["Água Mineral 500ml", 2.49, 100],
    ["Gelo 1kg", 4.99, 80],
    ["Gelo 5kg", 14.99, 40],
    ["Amendoim Torrado 200g", 6.99, 50],
    ["Batata Chips 150g", 7.49, 45],
    ["Torresmo Pururuca 100g", 8.99, 30],
    ["Queijo Provolone Desidratado 100g", 12.99, 20],
    ["Salgadinho Doritos 140g", 9.99, 35],
    ["Salgadinho Cheetos 140g", 8.99, 40],
    ["Azeitona Verde 200g", 6.99, 25],
    ["Picles 300g", 7.99, 20],
    ["Carvão para Churrasco 5kg", 19.99, 30],
    ["Espeto de Carne 300g", 14.99, 25],
    ["Espeto de Frango 300g", 12.99, 30],
    ["Espeto de Queijo Coalho 250g", 11.99, 20]
]
'''