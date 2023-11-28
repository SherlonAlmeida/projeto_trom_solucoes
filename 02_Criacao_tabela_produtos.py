import sqlite3
conexao = sqlite3.connect("bdTrom.sqlite3")
cursor = conexao.cursor()

tabela_produtos = """
CREATE TABLE Produtos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    descricao TEXT(100),
    preco DECIMAL
)"""

conexao.execute(tabela_produtos)

conexao.commit()
conexao.close()