import sqlite3
from gerenciar_clientes import * #Importa as funções do arquivo gerenciar_clientes.py

conexao = sqlite3.connect("bdTrom.sqlite3")
cursor = conexao.cursor()
###################################################

print("---- Seja bem-vind@ à TROM SOLUÇÕES ----")
while True:
    print("\nOpções: 1) Cadastrar cliente, 2) Mostrar clientes, 3) Deletar clientes, 4)Atualizar clientes, 0) Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0: #Finaliza o programa
        print("Programa finalizado!")
        break
    elif opcao == 1: #Cadastro de clientes
        cadastrar_clientes(conexao)
    elif opcao == 2: #Mostrar clientes
        mostrar_clientes(conexao)
    elif opcao == 3: #Deletar clientes
        deletar_clientes(conexao)
    elif opcao == 4: #Atualizar clientes
        atualizar_clientes(conexao)      
    else:
        print("Opção inválida!")

###################################################
conexao.commit()
conexao.close()