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
"""class Contagem:
    def __init__(self, inicio, fim):
        self.fim = fim
        self.atual = inicio - 1
    
    def contar_todos(self):
        print("Contagem: ", end="")
        for i in range(self.inicio, self.fim+1, 1):
            print(i, end=" ")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.atual >= self.fim:
            print("O limite da contagem foi excedido!")
            raise StopIteration
        
        self.atual += 1
        return self.atual

contador = Contagem(1, 5)
#contador.contar_todos()
#Iterador (Um a um por NEXT())
for i in range(10):
    try:
        print(contador.__next__())
    except StopIteration:
        print("Limite Excedido!")
        break"""

#Iteradores (baseados em Classes)
"""class IteraPessoas:
    def __init__(self, pessoas):
        self.pessoas = pessoas
        self.indice  = 0
        self.tamanho = len(pessoas)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice > self.tamanho-1:
            print("O limite da contagem foi excedido!")
            raise StopIteration
        
        pessoa_atual = self.pessoas[self.indice]
        self.indice += 1
        return pessoa_atual

pessoas = [
    {"Nome": "Sherlon", "Idade": 28},
    {"Nome": "Fabio", "Idade": 28},
    {"Nome": "Maria", "Idade": 18},
    {"Nome": "João", "Idade": 45},
    {"Nome": "Lucas", "Idade": 32}
]

dadosIter = IteraPessoas(pessoas)
for i in range(10):
    try:
        print(dadosIter.__next__())
    except StopIteration:
        print("Limite Excedido!")
        break"""