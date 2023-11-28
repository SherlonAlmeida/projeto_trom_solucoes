from gerenciar_clientes import mostrar_clientes
from gerenciar_produtos import mostrar_produtos

def menu_vendas(conn):
    print("\nOpções: 1) Realizar venda, 2) Mostrar vendas, 0) Voltar ao menu anterior")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0: #Finaliza o programa
        print("Voltando ao menu anterior!")
    elif opcao == 1: #Realizar venda
        realizar_venda(conn)
    elif opcao == 2: #Mostrar vendas
        mostrar_vendas(conn)    
    else:
        print("Opção inválida!")

def realizar_venda(conn):
    cursor = conn.cursor()
    mostrar_clientes(conn)
    cliente_id = int(input("Digite o ID do Cliente: "))
    mostrar_produtos(conn)
    produto_id = int(input("Digite o ID do Produto: "))
    
    comando_sql = """INSERT INTO Vendas (cliente_id, produto_id) VALUES (?, ?);"""
    valores = [cliente_id, produto_id]
    cursor.execute(comando_sql, valores)
    conn.commit()

def mostrar_vendas(conn):
    cursor = conn.cursor()
    #comando_sql = """SELECT * FROM Vendas;"""

    #comando_sql = """
    #    SELECT
    #        Clientes.id, Clientes.nome, Vendas.cliente_id
    #    FROM Vendas
    #    INNER JOIN Clientes ON Vendas.cliente_id=Clientes.id;
    #"""

    #comando_sql = """
    #    SELECT
    #        Produtos.id, Produtos.descricao, Vendas.produto_id
    #    FROM Vendas
    #    INNER JOIN Produtos ON Vendas.produto_id=Produtos.id;
    #"""

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
        #print(dado)
        print(f"O cliente {cliente} comprou o produto: {produto}")



