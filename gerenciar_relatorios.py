def menu_relatorios(conn):
    print("\nOpções: 1) Mostrar Vendas, 0) Voltar ao menu anterior")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0: #Finaliza o programa
        print("Voltando ao menu anterior!")
    elif opcao == 1: #Realizar venda
        mostrar_vendas(conn)
    else:
        print("Opção inválida!")

def mostrar_vendas(conn):
    cursor = conn.cursor()
    comando_sql = """SELECT * FROM Vendas;"""
   
    comando_sql = """
        SELECT
            Clientes.id, Clientes.nome, Vendas.cliente_id, Produtos.id, Produtos.descricao, Vendas.produto_id
        FROM Vendas
        INNER JOIN Clientes ON Vendas.cliente_id=Clientes.id
        INNER JOIN Produtos ON Vendas.produto_id=Produtos.id
    """

    cursor.execute(comando_sql)
    dados_recuperados = cursor.fetchall()
    for dado in dados_recuperados:
        cliente = dado[1]
        produto = dado[4]
        cliente_id, cliente_nome, venda_cliente_id, produto_id, produto_descricao, venda_produto_id = dado
        print(f"O cliente {cliente_nome} (ID: {cliente_id}) comprou o produto: {produto_descricao} (ID: {produto_id})")