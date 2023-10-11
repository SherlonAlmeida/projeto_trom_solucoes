import sqlite3
conexao = sqlite3.connect("bdTrom.sqlite3")
cursor = conexao.cursor()
###################################################

print("---- Seja bem-vind@ à TROM SOLUÇÕES ----")
while True:
    print("\nOpções: 1) Cadastrar cliente, 2) Mostrar clientes, 0) Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0: #Finaliza o programa
        print("Programa finalizado!")
        break
    elif opcao == 1: #Cadastro de clientes
        nome = input("Digite o seu nome: ")
        telefone = input("Digite o seu telefone: ")
        cpf = input("Digite o seu CPF: ")
        comando_sql = """INSERT INTO Clientes (nome, telefone, cpf) VALUES (?, ?, ?);"""
        valores = [nome, telefone, cpf]
        cursor.execute(comando_sql, valores)
        conexao.commit()
    elif opcao == 2: #Mostrar clientes
        comando_sql = """SELECT * FROM Clientes;"""
        cursor.execute(comando_sql)
        dados_recuperados = cursor.fetchall()
        for dado in dados_recuperados:
            print(dado)
    else:
        print("Opção inválida!")

###################################################
conexao.commit()
conexao.close()