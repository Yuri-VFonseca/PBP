def delete_usuario(chave, senha, usuario_logado): 
    usuario = buscar_usuario(chave, senha)
    
    if usuario is None: 
        print("Usuário não encontrado")
        return
    if usuario["Senha"] != 

    # Permissões de deleção para diferentes tipos de usuário
    if usuario_logado["Tipo"] == "usuario": 
        if usuario_logado["Nome"] != usuario["Nome"]: 
            print("Você não tem permissão para deletar o perfil de outro usuário")
            return
    elif usuario_logado["Tipo"] == "funcionario": 
        if usuario["Tipo"] == "funcionario" or usuario["Tipo"] == "gerente": 
            print("Você não tem permissão para deletar o perfil de outro funcionário ou gerente")
            return
    elif usuario_logado["Tipo"] == "gerente": 
        if usuario["Tipo"] == "gerente": 
            print("Gerentes não podem deletar outros gerentes")
            return

    # Deletar o usuário
    usuarios_atualizados = []
    with open('usuarios.csv', 'r', newline='', encoding="UTF-8") as file: 
        reader = csv.reader(file)
        next(reader, None)
        for linha in reader: 
            if len(linha) < 4: 
                continue
            nome, senha_armazenada, tipo, n_login = linha
            # Se o nome ou número de login corresponde ao usuário a ser deletado, ele será ignorado
            if nome == usuario["Nome"] or str(n_login) == str(usuario["Número de login"]): 
                continue
            usuarios_atualizados.append(linha)

    with open('usuarios.csv', 'w', newline='', encoding="UTF-8") as file: 
        writer = csv.writer(file)
        writer.writerow(["Nome", "Senha", "Tipo", "Número de login"])  # Cabeçalho correto
        writer.writerows(usuarios_atualizados)
    print(f"Usuário {usuario['Nome']} excluído com sucesso!")

