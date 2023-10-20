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
    #Você vai colocar o seu código aqui
    pass