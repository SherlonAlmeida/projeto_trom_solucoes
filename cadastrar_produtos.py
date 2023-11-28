import sqlite3
conexao = sqlite3.connect("bdTrom.sqlite3")
cursor = conexao.cursor()

for i in range(5): #Cadastrar 5 produtos
    descricao = input("Digite a descrição do produto: ")
    preco = input("Digite o preço do produto: ")
    comando_sql = """INSERT INTO Produtos (descricao, preco) VALUES (?, ?);"""
    valores = [descricao, preco]
    cursor.execute(comando_sql, valores)
    conexao.commit()

conexao.commit()
conexao.close()