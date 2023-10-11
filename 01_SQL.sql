CREATE TABLE Clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT(100),
    telefone TEXT(15),
    cpf TEXT(15)
);

INSERT INTO Clientes (nome, telefone, cpf) VALUES ("Sherlon", "(099) 99999-9999", "333.333.333-33");

SELECT * FROM Clientes;
