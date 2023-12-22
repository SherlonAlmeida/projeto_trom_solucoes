from gerenciar_clientes import mostrar_clientes
from gerenciar_produtos import mostrar_produtos

def menu_vendas(conn):
    print("\nOpções: 1) Realizar venda, 0) Voltar ao menu anterior")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0: #Finaliza o programa
        print("Voltando ao menu anterior!")
    elif opcao == 1: #Realizar venda
        realizar_venda(conn)     
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