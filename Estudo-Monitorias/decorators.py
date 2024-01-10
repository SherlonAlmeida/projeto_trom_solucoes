#Lidando com o comportamento de Funções
"""def bom_dia():
    return "Bom dia!"

def boa_tarde():
    return "Boa tarde!"

def exemplo():
    funcoes = [bom_dia, boa_tarde]
    for cumprimento in funcoes:
        print(f"Olá, {cumprimento()}")

exemplo()"""

#Decorators (Forma 1)
"""def minha_personalizacao_da_funcao(func):
    def mofificacao_realizada():
        print("1) Adicionei esta linha ANTES da execucao da funcao original!")
        func() #Chamada da função original
        print("3) Adicionei esta linha DEPOIS da execucao da funcao original!")
    return mofificacao_realizada
 
def funcao_a_ser_personalizada():
    print("2) Função ORIGINAL a ser adaptada!!")
 
funcao_a_ser_personalizada = minha_personalizacao_da_funcao(funcao_a_ser_personalizada)
funcao_a_ser_personalizada()"""

#Decorators (Forma 2)
"""def minha_personalizacao_da_funcao(func):
    def mofificacao_realizada():
        print("1) Adicionei esta linha ANTES da execucao da funcao original!")
        func() #Chamada da função original
        print("3) Adicionei esta linha DEPOIS da execucao da funcao original!")
    return mofificacao_realizada

@minha_personalizacao_da_funcao
def funcao_a_ser_personalizada():
    print("2) Função ORIGINAL a ser adaptada!!")
 
funcao_a_ser_personalizada()"""

#Exemplo prático (Strings)
"""def preprocessamento_maiusculo(func):
    def modificacoes():
        novo_texto = func().upper()
        return novo_texto
    return modificacoes

@preprocessamento_maiusculo
def obtem_texto():
    texto = input("Digite uma mensagem: ")
    return texto

print(obtem_texto())"""

#Pendente: fazer o exercício da semana.