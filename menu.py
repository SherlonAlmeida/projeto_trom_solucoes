import sqlite3
from gerenciar_clientes import * #Importa as funções do arquivo gerenciar_clientes.py

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
        cadastrar_clientes(conexao)
    elif opcao == 2: #Mostrar clientes
        #TAREFA FÁBIO: adaptar este trecho de código em uma função em outro arquivo.
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