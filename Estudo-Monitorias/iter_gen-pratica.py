#Sem Iteradores e Geradores
#Indices:     0        1        2        3
#dados = ["Sherlon", "Fabio", "Maria", "João"]

#for pessoa in dados:
#    print(pessoa)

# for indice in range(1, 3): #[inicial, final)
#     print(dados[indice])

#Geradores (usando bibliotecas)
# dados = iter(["Sherlon", "Fabio", "Maria", "João"])
# print(dados.__next__()) #Mostra Sherlon
# print(dados.__next__()) #Mostra Fabio
# print(next(dados))      #Mostra Maria

#Geradores (baseados em Funções)
#Return: Retorna um valor da função e FINALIZA a execução!
#Yield:  Retorna um valor da função, porém LEMBRA onde parou anteriormente!
# def minha_func_iter(dados):
#     for dado in dados:
#         yield dado

# dados = ["Sherlon", "Fabio", "Maria", "João"]
# meu_gerador = minha_func_iter(dados)
# print(next(meu_gerador))
# print(next(meu_gerador))

#Exemplo prático:
#Aplicabilidade: economia de memória e melhora de performance durante a execução.
#Vantagens: Fragmentando a execução de dados em LOTES
"""imagens = [[2,8,9,5],     #Armazena PARTE das imagens para o PRIMEIRO lote de execução.
           [1,2,3,4],     #Armazena PARTE das imagens para o SEGUNDO lote de execução.
           [2,4,6,8]]     #Armazena PARTE das imagens para o TERCEIRO lote de execução.

def processa_dados(lote_atual_dados):
    print(lote_atual_dados)

#Cria a variável com a SEPARAÇÃO em Lotes de Execução
dados_totais = iter(imagens)
for lote in range(5):
    try:
        lote_atual = next(dados_totais)
        processa_dados(lote_atual)
    except StopIteration:
        print("O limite de lotes foi alcançado!")
        break #Finalizar, uma vez que chegou ao fim dos lotes!"""

#Quem determina a quantidade máxima é VOCÊ.
"""def potencia(max):
    for i in range(max):
        yield i**2
variavel_potencia = potencia(10)
print(next(variavel_potencia))
print(next(variavel_potencia))
print(next(variavel_potencia))
print(next(variavel_potencia))
print(next(variavel_potencia))"""

#Se você não sabe a quantidade de elementos, é preciso contar!
"""from random import randint
def exemplo(dados):
    for dado in dados:
        yield dado

dados = iter([randint(1, 50) for i in range(randint(500, 1000))])
meu_gen = exemplo(dados)
contagem = 0 #Quantidade de elementos do meu Iter ou meu Generator
while True:
    try:
       next(meu_gen)
       contagem += 1
    except StopIteration:
        print(f"Existem {contagem} elementos no iter.")
        break"""

#Iteradores (baseados em Classes)

