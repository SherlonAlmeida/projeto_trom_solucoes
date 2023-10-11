import sqlite3
conexao = sqlite3.connect("bdTrom.sqlite3")
cursor = conexao.cursor()
###################################################
#RECUPERAR INFORMAÇÕES SALVAS NO BANCO DE DADOS (Comando SELECT)
comando_sql = """SELECT * FROM Clientes;"""
cursor.execute(comando_sql)
dados_recuperados = cursor.fetchall()

for dado in dados_recuperados:
    print(dado)

###################################################
conexao.commit()
conexao.close()