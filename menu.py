import sqlite3
from gerenciar_clientes import * #Importa as funções do arquivo gerenciar_clientes.py
from gerenciar_produtos import * #Importa as funções do arquivo gerenciar_produtos.py
from gerenciar_vendas import *   #Importa as funções do arquivo gerenciar_vendas.py
from gerenciar_relatorios import *

conexao = sqlite3.connect("bdTrom.sqlite3")
cursor = conexao.cursor()
###################################################

print("---- Seja bem-vind@ à TROM SOLUÇÕES ----")
while True:
    print("\nOpções: 1) Clientes, 2) Produtos, 3) Vendas, 4)Relatórios, 0) Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0: #Finaliza o programa
        print("Programa finalizado!")
        break
    elif opcao == 1:
        menu_clientes(conexao)
    elif opcao == 2:
        menu_produtos(conexao)
    elif opcao == 3:
        menu_vendas(conexao)
    elif opcao == 4:
        menu_relatorios(conexao)
    else:
        print("Opção inválida!")

###################################################
conexao.commit()
conexao.close()