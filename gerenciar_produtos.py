def menu_produtos(conn):
    print("\nOpções: 1) Cadastrar produto, 2) Mostrar produtos, 3) Deletar produtos, 4)Atualizar produtos, 0) Voltar ao menu anterior")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0: #Finaliza o programa
        print("Voltando ao menu anterior!")
    elif opcao == 1: #Cadastro de produtos
        cadastrar_produtos(conn)
    elif opcao == 2: #Mostrar produtos
        mostrar_produtos(conn)
    elif opcao == 3: #Deletar produtos
        deletar_produtos(conn)
    elif opcao == 4: #Atualizar clientes
        atualizar_produtos(conn)      
    else:
        print("Opção inválida!")

def cadastrar_produtos(conn):
    cursor = conn.cursor()
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    comando_sql = """INSERT INTO Produtos (descricao, preco) VALUES (?, ?);"""
    valores = [descricao, preco]
    cursor.execute(comando_sql, valores)
    conn.commit()
    print("PRODUTO CADASTRADO COM SUCESSO!")

def mostrar_produtos(conn):
    cursor = conn.cursor()
    comando_sql = """SELECT * FROM Produtos;"""
    cursor.execute(comando_sql)
    dados_recuperados = cursor.fetchall()
    for dado in dados_recuperados:
        print(dado)

def atualizar_produtos(conn): #UPDATE
    cursor = conn.cursor()
    mostrar_produtos(conn)
    id = int(input("Digite o ID do produto a ser atualizado: "))
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    comando_sql = """UPDATE Produtos SET descricao = ?, preco = ? where id = ?"""
    valores = [descricao, preco, id]
    cursor.execute(comando_sql, valores)
    conn.commit()
    print("PRODUTO ATUALIZADO COM SUCESSO!")

def deletar_produtos(conn):
    cursor = conn.cursor()
    mostrar_produtos(conn) #Mostra produtos
    id = int(input("Digite o ID do produto a ser excluido: "))
    comando_sql = """DELETE FROM Produtos WHERE id = ?"""
    valores = [id]
    cursor.execute(comando_sql, valores)
    conn.commit()
    print("PRODUTO DELETADO COM SUCESSO!")