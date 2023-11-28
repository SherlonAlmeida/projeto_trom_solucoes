import sqlite3
conexao = sqlite3.connect("bdTrom.sqlite3")
cursor = conexao.cursor()

tabela_vendas = """
CREATE TABLE Vendas (
    cliente_id INTEGER,
    produto_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);"""

conexao.execute(tabela_vendas)

conexao.commit()
conexao.close()