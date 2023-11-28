import sqlite3
conexao = sqlite3.connect("bdTrom.sqlite3")
cursor = conexao.cursor()
###################################################

#CRIA O BANCO DE DADOS + A TABELA CLIENTES (Comando CREATE TABLE)
comando_sql = """CREATE TABLE Clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT(100),
    telefone TEXT(15),
    cpf TEXT(15)
)"""

cursor.execute(comando_sql)

###################################################
conexao.commit()
conexao.close()