def cadastrar_clientes(conn):
    cursor = conn.cursor()
    nome = input("Digite o seu nome: ")
    telefone = input("Digite o seu telefone: ")
    cpf = input("Digite o seu CPF: ")
    comando_sql = """INSERT INTO Clientes (nome, telefone, cpf) VALUES (?, ?, ?);"""
    valores = [nome, telefone, cpf]
    cursor.execute(comando_sql, valores)
    conn.commit()

def mostrar_clientes(conn):
    cursor = conn.cursor()
    comando_sql = """SELECT * FROM Clientes;"""
    cursor.execute(comando_sql)
    dados_recuperados = cursor.fetchall()
    for dado in dados_recuperados:
        print(dado)

def atualizar_clientes(conn): #UPDATE
    pass

def deletar_clientes(conn):
    cursor = conn.cursor()
    mostrar_clientes(conn) #Mostra clientes
    id = int(input("Digite o ID do cliente a ser excluido: "))
    comando_sql = """DELETE FROM Clientes WHERE id = ?"""
    valores = [id]
    cursor.execute(comando_sql, valores)
    conn.commit()