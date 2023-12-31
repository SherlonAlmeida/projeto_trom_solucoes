def menu_clientes(conn):
    print("\nOpções: 1) Cadastrar cliente, 2) Mostrar clientes, 3) Deletar clientes, 4)Atualizar clientes, 0) Voltar ao menu anterior")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0: #Finaliza o programa
        print("Voltando ao menu anterior!")
    elif opcao == 1: #Cadastro de clientes
        cadastrar_clientes(conn)
    elif opcao == 2: #Mostrar clientes
        mostrar_clientes(conn)
    elif opcao == 3: #Deletar clientes
        deletar_clientes(conn)
    elif opcao == 4: #Atualizar clientes
        atualizar_clientes(conn)      
    else:
        print("Opção inválida!")

def cadastrar_clientes(conn):
    cursor = conn.cursor()
    nome = input("Digite o seu nome: ")
    telefone = input("Digite o seu telefone: ")
    cpf = input("Digite o seu CPF: ")
    comando_sql = """INSERT INTO Clientes (nome, telefone, cpf) VALUES (?, ?, ?);"""
    valores = [nome, telefone, cpf]
    cursor.execute(comando_sql, valores)
    conn.commit()
    print("CLIENTE CADASTRADO COM SUCESSO!")

def mostrar_clientes(conn):
    cursor = conn.cursor()
    comando_sql = """SELECT * FROM Clientes;"""
    cursor.execute(comando_sql)
    dados_recuperados = cursor.fetchall()
    for dado in dados_recuperados:
        print(dado)

def atualizar_clientes(conn): #UPDATE
    cursor = conn.cursor()
    mostrar_clientes(conn)
    id = int(input("Digite o ID do cliente a ser atualizado: "))
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    cpf = input("Digite o CPF: ")
    comando_sql = """UPDATE Clientes SET nome = ?, telefone = ?, cpf = ? where id = ?"""
    valores = [nome, telefone, cpf, id]
    cursor.execute(comando_sql, valores)
    conn.commit()
    print("CLIENTE ATUALIZADO COM SUCESSO!")

def deletar_clientes(conn):
    cursor = conn.cursor()
    mostrar_clientes(conn) #Mostra clientes
    id = int(input("Digite o ID do cliente a ser excluido: "))
    comando_sql = """DELETE FROM Clientes WHERE id = ?"""
    valores = [id]
    cursor.execute(comando_sql, valores)
    conn.commit()
    print("CLIENTE DELETADO COM SUCESSO!")