'''
Fazer CRUD -  Create, Read, Update and Delete
Usuários - Controle de acesso (usuario (ver itens), gerente (ver, criar, reduzir e aumentar n de itens e colocar novos preços) e funcionário (ver e reduzir ou aumentar n de itens)
Organizar em um doc (.csv)
Produtos ou serviços - armazernar em um .csv separado, aplicar crud
'''
import random
import csv
# senhas mestres
senha_funcionario = "@charliebrownjr72"
senha_gerente = "#redhotchilipeppers_1983"
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
    with open('produtos.csv', 'r', newline='', encoding="UTF-8") as file: 
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
def update_produto(chave, nome=None, preco=None, quantidade=None, usuario_tipo="usuario"): 
    if usuario_tipo == "usuario": 
        print("Você não tem permissão para alterar produtos")
        return
    if usuario_tipo == "funcionario": 
        if nome or preco: 
            print("Funcionários podem alterar apenas a quantidade")
            return
        else: 
            pass
    if usuario_tipo == "gerente": 
        pass
    produtos_atualizados = []
    with open('produtos.csv', 'r', newline='', encoding="UTF-8") as file: 
        reader = csv.reader(file)
        next(reader, None)
        for linha in reader: 
            if linha: 
                nomeproduto, preco_atual, quantidade_atual, codigo = linha
                if nomeproduto == chave or int(codigo) == chave:
                    if nome: 
                        nomeproduto = nome
                    if preco is not None: 
                        preco_atual = preco
                    if quantidade is not None: 
                        quantidade_atual = int(quantidade_atual) + quantidade
            produtos_atualizados.append([nomeproduto, preco_atual, quantidade_atual, codigo])
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
def create_usuario(nome, senha): 
    tipo = "cliente"
    n_login = random.randint(100,1000)
    if senha == senha_funcionario: 
        tipo = "funcionário"
        n_login = random.randint(11, 99)
    elif senha == senha_gerente: 
        tipo = "gerente"
        n_login = random.randint(1,10)
    usuario = [nome, senha, tipo, n_login]
    with open('usuarios.csv', 'a', newline='', encoding="UTF-8") as file: 
        writer = csv.writer(file)
        writer.writerow(usuario)
#read
def buscar_usuario(chave, senha): 
    with open('usuarios.csv', 'r', newline='', encoding="UTF-8") as file: 
        reader = csv.reader(file)
        next(reader, None)
        for linha in reader: 
            if len(linha) < 4: 
                continue
            nome, senha_armazenada, tipo, n_login = linha
            if chave == nome or str(n_login) == str(chave):
                if senha ==  senha_armazenada: 
                return {"Nome": nome, "Tipo": tipo, "Número de login": n_login} # chave - produto
            else: 
                print("Senha incorreta")
                return None
        print("Usuário não encontrado")
        return None
#update

#delete

#cliente (ver produto, alterar suas info)

#funcionario (ver, dar baixa e aumentar, atualizar clientes e criar)

#gerente (todo o restante + cadastrar novos produtos e alterar preços, CRUD clientes)

#menus 

# Variaveis, listas e cabeçalho
with open("produtos.csv", 'w', newline="", encoding="UTF-8") as file: 
    writer = csv.writer(file)
    writer.writerow(["Nome", "Preço", "Quantidade", "Código"])


# Menu


'''
produtos_lista =[
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
    ["Batida de Côco 300ml", 9.99, 40],
    ["Batida de Morango 300ml", 10.99, 35],
    ["Batida de Limão 300ml", 8.99, 30],
    ["Energético Red Bull 250ml", 9.99, 50],
    ["Energético Red Bull 473ml", 14.99, 40],
    ["Energético Monster 250ml", 10.99, 45],
    ["Energético Monster 473ml", 14.99, 35],
    ["Refrigerante Coca-Cola 2L", 8.99, 60],
    ["Refrigerante Guaraná Antarctica 2L", 7.99, 55],
    ["Refrigerante Sprite 2L", 8.49, 50],
    ["Suco de Laranja Natural 1L", 12.99, 30],
    ["Suco de Laranja 300ml", 5.99, 40],
    ["Suco de Abacaxi 300ml", 5.99, 35],
    ["Suco de Manga 300ml", 6.49, 30],
    ["Suco de Uva 300ml", 6.49, 25],
    ["Água Mineral 500ml", 2.49, 100],
    ["Água Sem Gás 500ml", 3.49, 50],
    ["Água Tônica Schweppes 350ml", 5.99, 40],
    ["Gelo 1kg", 4.99, 80],
    ["Gelo 5kg", 14.99, 40],
    ["Porção de Batata Frita 300g", 10.99, 40],
    ["Porção de Onion Rings 200g", 9.99, 30],
    ["Porção de Fritas com Cheddar 250g", 12.99, 35],
    ["Porção de Frango Empanado 250g", 14.99, 20],
    ["Porção de Isca de Frango 300g", 15.99, 25],
    ["Porção de Carne de Panela 300g", 18.99, 20],
    ["Espeto de Carne 300g", 14.99, 25],
    ["Espeto de Frango 300g", 12.99, 30],
    ["Espeto de Queijo Coalho 250g", 11.99, 20],
    ["Mini Hambúrguer (5 unidades)", 19.99, 20],
    ["Hambúrguer Artesanal (200g)", 21.99, 30],
    ["Hambúrguer de Costela (250g)", 24.99, 15],
    ["Hambúrguer de Frango (200g)", 18.99, 20],
    ["Hambúrguer Vegetariano (200g)", 22.99, 12],
    ["Macarrão ao Alho e Óleo", 16.99, 15],
    ["Macarrão à Carbonara", 18.49, 12],
    ["Macarrão à Bolonhesa", 19.99, 18],
    ["Macarrão com Frango Grelhado", 20.99, 10],
    ["Bala de Caramelo", 2.49, 50],
    ["Bala de Menta", 1.99, 60],
    ["Brigadeiro de Colher", 5.99, 40],
    ["Picolé de Fruta (Coco, Limão, Maracujá)", 4.99, 50],
    ["Picolé de Chocolate (Chocolate, Nutella)", 5.99, 45],
    ["Picolé de Creme (Baunilha, Morango)", 5.49, 30]
]

'''