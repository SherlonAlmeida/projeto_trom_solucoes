CREATE TABLE Clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT(100),
    telefone TEXT(15),
    cpf TEXT(15)
);
INSERT INTO Clientes (nome, telefone, cpf) VALUES ("Sherlon", "(099) 99999-9999", "333.333.333-33");
SELECT * FROM Clientes;

-- Tarefa: Criar as seguintes tabelas no banco.
CREATE TABLE Produtos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    descricao TEXT(100),
    preco DECIMAL
)

CREATE TABLE Vendas (
    cliente_id INTEGER,
    produto_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);