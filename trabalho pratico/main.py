'''
Fazer CRUD -  Create, Read, Update and Delete
Usuários - Controle de acesso (usuario (ver itens), gerente (ver, criar, reduzir e aumentar n de itens e colocar novos preços) e funcionário (ver e reduzir ou aumentar n de itens)
Organizar em um doc (.csv)
Produtos ou serviços - armazernar em um .csv separado, aplicar crud
'''
import random
import csv
import re
import os
# senhas mestres
senha_funcionario = "@CharlieBrownJR72"
senha_gerente = "#RedHotChiliPeppers_1983"
#funcoes - produtos
produtos = []
cabecalho_produtos = ["Nome", "Preço", "Quantidade", "Código"]
cabecalho_usuarios = ["Nome", "Senha", "Tipo", "Número de login"]
#create
def create_produto(produto, cabecalho): 
    if not os.path.exists("produtos.csv"): 
        with open("produtos.csv", 'w', newline='', encoding="UTF-8") as file: 
            writer = csv.writer(file)
            writer.writerow(cabecalho)
    try: 
        with open('produtos.csv', 'r', newline='', encoding="UTF-8") as file: 
            pass
    except FileNotFoundError: 
        with open('produtos.csv', 'w', newline='', encoding='UTF-8') as file: 
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Preço', 'Quantidade', 'Código'])
    with open('produtos.csv', 'a', newline='', encoding="UTF-8") as file: 
        writer = csv.writer(file)
        writer.writerow(produto)
            # criar colunas na planilha 
def info_produtos(nome, preco, quantidade):
    codigo = random.randint(10000000, 999999999) # criar codigo aleatorio
    produto = [nome, preco, quantidade, codigo]
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
def senha_valida(chave): 
    if (len(chave) >= 8 and re.search(r"\d", chave) and re.search(r"[!@#$%¨&*(){}+=§^,.:;<>[]]", chave) and re.search(r"[A-Z]", chave) and re.search(r"[a-z]", chave)):
        return True
    return False 
def create_usuario(nome, senha, opcao): 
    if opcao == 5: 
        if senha != senha_funcionario: 
            print("Senha incorreta")
            return False
        tipo = "funcionário"
        n_login = random.randint(10,99)
    elif opcao == 6: 
        if senha != senha_gerente:
            print("Senha incorreta")
            return False
        tipo = "gerente"
        random.randint(1,10)
    elif opcao == 4: 
        if senha_valida(senha) == False: 
            print("Senha inválida para usuário! Deve conter ao menos 8 caracteres, contendo número, maiúscula, minúscula e caracter especial")
            return False
        tipo = "cliente"
        n_login = random.randint(1000, 1999)
    else: 
        print("Opção válida")
        return False
    usuario = [nome, senha, tipo, n_login]
    with open("usuarios.csv", 'a', newline='', encoding="UTF-8") as file: 
        writer = csv.writer(file)
        writer.writerow(usuario)
#read
def buscar_usuario(chave, senha=None): 
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
def update_usuario(chave, senha, novo_nome=None, nova_senha=None, novo_tipo=None, usuario_logado=None): 
    usuario = buscar_usuario(chave, senha)
    if usuario is None: 
        print("Usuário não encontrado")
        return 
    if usuario["Senha"] != senha: 
        print("Senha incorreta")
        return
    if usuario_logado["Tipo"] == "cliente":
        if usuario_logado["Nome"] != usuario["Nome"]:
            print("Você não tem permissão para alterar o perfil de outro usuário")
            return
        if novo_tipo: 
            print("Você não pode alterar o seu tipo de usuário")
        return
    elif usuario_logado["Tipo"] == "funcionario": 
        if usuario_logado["Nome"] != usuario["Nome"] and usuario["Tipo"] in ["funcionario", "gerente"]:
            print("Você não tem permissão para alterar o perfil de outro funcionário ou gerente")
        return
    elif usuario_logado["Tipo"] == "gerente": 
        pass
    usuarios_atualizados = []
    with open('usuarios.csv', 'r', newline='', encoding="UTF-8") as file: 
        reader = csv.reader(file)
        next(reader, None)
        for linha in reader: 
            if len(linha) < 4: 
                continue
            nome, senha_atual, tipo, n_login = linha
            if nome == usuario["Nome"] or str(n_login) == str(usuario["Número de login"]): 
                if novo_nome: 
                    nome = novo_nome
                if nova_senha: 
                    senha_atual = nova_senha
                if novo_tipo and usuario_logado["Tipo"] == "gerente": 
                    tipo = novo_tipo
            usuarios_atualizados.append([nome, senha_atual, tipo, n_login])
    with open('usuarios.csv', 'w', newline='', encoding="UTF-8") as file: 
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Senha', 'Tipo', 'Número de login'])
        writer.writerows(usuarios_atualizados)
#delete
def delete_usuario(chave, senha, usuario_logado): 
    usuario = buscar_usuario(chave, senha)
    if usuario is None: 
        print("Usuário não encontrado")
        return 
    if usuario["Senha"] != senha: 
        print("Senha incorreta")
        return
    if usuario_logado["Tipo"] == "cliente":
        if usuario_logado["Nome"] != usuario["Nome"]:
            print("Você não tem permissão para deletar o perfil de outro usuário")
            return
    elif usuario_logado["Tipo"] == "funcionario": 
        if usuario_logado["Nome"] != usuario["Nome"] and usuario["Tipo"] in ["funcionario", "gerente"]:
            print("Você não tem permissão para deletar o perfil de outro funcionário ou gerente")
            return
    elif usuario_logado["Tipo"] == "gerente": 
        pass
    usuarios_atualizados = []
    with open('usuarios.csv', 'r', newline='', encoding="UTF-8") as file: 
        reader = csv.reader(file)
        next(reader, None)
        for linha in reader: 
            if len(linha) < 4: 
                continue
            nome, senha_armazenada, tipo, n_login = linha
            if nome == usuario["Nome"] or str(n_login) == str(usuario["Número de login"]):
                continue
            usuarios_atualizados.append(linha)
    with open('usuarios.csv', 'w', newline='', encoding='UTF-8') as file: 
        writer = csv.writer(file)
        writer.writerow(["Nome", "Senha", "Quantidade", "Número de login"])
        writer.writerows(usuarios_atualizados)
    print(f"Usuário {usuario["Nome"]} excluído com sucesso!")
#cliente (ver produto, alterar suas info)

#funcionario (ver, dar baixa e aumentar, atualizar clientes e criar)

#gerente (todo o restante + cadastrar novos produtos e alterar preços, CRUD clientes)

#menus 
def menu_usuario(): 
    while True: 
        print("----- Menu de Usuário -----")
        print("1 - Entrar cliente")
        print("2 - Entrar funcionário")
        print("3 - Entrar gerente")
        print("4 - Criar usuário")
        print("5 - Criar funcionário")
        print("6 - Criar gerente")
        print("7 - Editar perfil")
        print("8 - Deleter perfil")
        print("0 - Sair")
        try: 
            opcao = int(input("Opção: "))
        except ValueError: 
            print("Escolha uma opção válida")
            continue
        if opcao == 0: 
            print("ENCERRADO")
            break
        elif opcao == 1:
            nome = input("Digite o nome: ")
            senha = input("Digite a senha: ")
            usuario = buscar_usuario(nome, senha)
            if usuario: 
                print(f"Bem-vindo, {usuario["Nome"]}!")
            else: 
                print("Usuário não encontrado ou senha incorreta")
        elif opcao == 2: 
            nome = input("Digite o nome: ")
            senha = input("Digite para funcionários: ")
            usuario = buscar_usuario(nome, senha)
            if usuario and usuario["Tipo"] == 'funcionario': 
                print(f"Bem-vindo, {usuario["Nome"]} (funcionário)!")
            else: 
                print("Usuário não encontrado, senha incorreta ou não é um funcionário")
        elif opcao == 3: 
            nome = input("Digite o nome: ")
            senha = input("Digite a senha: ")
            usuario = buscar_usuario(nome, senha)
            if usuario and usuario["Tipo"] == 'gerente': 
                print(f"Bem-vindo, {usuario["Nome"]} (gerente)!")
            else: 
                print("Usuário não encontrado, senha incorreta ou não é gerente")
        elif opcao == 4: 
            nome = input("Digite o nome: ")
            senha = input("Digite a senha: ")
            create_usuario(nome, senha, opcao)
            try: 
                print(f"Usuário {nome} criado com sucesso!")
            except Exception as e: 
                print(f"Usuário {nome} não foi criado")
        elif opcao == 5: 
            senha_mestre = input("Digite a senha mestre para criar um funcionário: ")
            if senha_mestre == senha_funcionario: 
                nome = input("Digite o nome: ")
                create_usuario(nome, senha_funcionario, opcao)
                print(f"Funcionário {nome} criado com sucesso!")
            else: 
                print("Senha mestre incorreta")
        elif opcao == 6: 
            senha_mestre = input("Digite a senha mestre para criar um funcionário: ")
            if senha_mestre == senha_gerente: 
                nome = input("Digite o nome: ")
                create_usuario(nome, senha_gerente, opcao)
                print(f"Gerente {nome} criado com sucesso!")
            else: 
                print("Senha mestre incorreta")
        elif opcao == 7: 
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            usuario_logado = buscar_usuario(nome, senha)
            if usuario_logado: 
                print(f"Bem-vindo, {usuario_logado['Nome']}!")
                novo_nome = input("Digite o novo nome (ou pressione Enter para manter): ")
                nova_senha = input("Digite a nova senha (ou pressione Enter para manter): ")
                novo_tipo = input("Digite o novo tipo (ou pressione Enter para manter): ").lower()
                update_usuario(nome, senha, novo_nome, nova_senha, novo_tipo, usuario_logado)
                print("Perfil atualizado com sucesso!")
            else: 
                ("Usuário não encotrado ou senha incorreta")

        elif opcao == 8: 
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            usuario_logado = buscar_usuario(nome, senha)
            if usuario_logado: 
                delete_usuario(nome, senha, usuario_logado)
                print(f"Usuário {nome} deletado com sucesso!")
            else:
                print("Usuário não encontrado ou sneha incorreta")
        else: 
            print("Escolha uma opção válida")
def menu_produtos(usuario_logado): 
    while True: 
        print("----- Menu de produtos ------")
        print("1 - Buscar produto")
        if usuario_logado["Tipo"] in ['funcionario', 'gerente']: 
            print("2 - Adicionar novo produto")
            print("3 - Editar produto")
            print("4 - Deletar produto")
        print("0 - Sair")
        try: 
            opcao = int(input("Opção: "))
        except ValueError: 
            print("Escolha uma opção válida")
            continue
        if opcao == 0: 
            print("Encerrando o menu de produtos...")
            break
        elif opcao == 1: 
            nome_produto = input("Digite o nome ou código do produto que deseja buscar: ")
            produto = buscar_produto(nome_produto)
            if produto: 
                print(produto)
            else: 
                print("Produto não encontrado")
        elif opcao == 2 and usuario_logado["Tipo"] == "gerente": 
            nome_produto = input("Digite o nome ou código do produto que deseja criar: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade inicial: "))
            info_produtos(nome_produto,preco,quantidade)
            print("Produto adicionado com sucesso! ")
        elif opcao == 3 and usuario_logado["Tipo"] in ["funcionario", 'gerente']: 
            nome_produto = input("Digite o nome ou código do produto que deseja editar: ") 
            print("1 - Adicionar estoque")
            print("2 - Reduzir estoque")
            opcao = int(input("Escolha uma opção: "))
            quantidade = int(input("Digite a quantidade: "))
            if opcao == 1: 
                update_produto(produto["Código"],quantidade=quantidade, usuario_tipo=usuario_logado["Tipo"])
                print(f"Estoque de {produto['Nome']} atualizado! Quantidade adicionada: {quantidade}")
            elif opcao == 2: 
                if produto['Quantidade'] >= quantidade: 
                    update_produto(produto['Código'], quantidade=quantidade,usuario_tipo=usuario_logado["Tipo"])
                    print(f"Estoque de {produto["Nome"]} atualizade! Quantidade reduzida: {quantidade}")
                else: 
                    print("Não há estoque suficiente para reduzir essa quantidade")
            elif opcao != 1 and opcao != 2: 
                print("Escolha uma opção válida")
            else: 
                print("Produto não encontrado")

        elif opcao == 4 and usuario_logado["Tipo"] == "gerente": 
            nome_produto = input("Digite o nome ou código do produto que deseja deletar: ")
            nome_produto = buscar_produto(nome_produto)
            if produto:  
                print("Deseja apagar o produto? ")
                print("1 - SIM")
                print("2 - Não")
                opcao = int(input())
                if opcao == 1: 
                    delete_produto(nome_produto["Código"])
                    print("Produto deletado com sucesso!")
                if opcao == 2: 
                    print("Produto não foi deletado")
            else: 
                print("Produto não encontrado")
        else: 
            print("Escolha uma opção válida")

menu_usuario()
menu_produtos()
# Variaveis, listas e cabeçalho
"""with open("produtos.csv", 'w', newline="", encoding="UTF-8") as file: 
    writer = csv.writer(file)
    writer.writerow(["Nome", "Preço", "Quantidade", "Código"])
"""

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