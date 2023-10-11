class Cliente:
    def __init__(self):
        self.nome = None
        self.telefone = None
        self.cpf = None
    
    def cadastro(self):
        print("---- Cadastro de Cliente ----")
        self.nome = input("Digite o nome: ")
        self.telefone = input("Digite o telefone: ")
        self.cpf = input("Digite o CPF: ")
    
    def mostra_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"CPF: {self.cpf}")

meus_clientes = [] #Armazenar os clientes

print("---- Seja bem-vind@ à TROM SOLUÇÕES ----")
while True:
    print("\nOpções: 1) Cadastrar cliente, 2) Mostrar clientes, 0) Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0: #Finaliza o programa
        print("Programa finalizado!")
        break
    elif opcao == 1: #Cadastro de clientes
        cliente = Cliente()
        cliente.cadastro()
        meus_clientes.append(cliente)
    elif opcao == 2: #Mostrar clientes
        print("---- Clientes cadastrados ----")
        for cliente in meus_clientes:
            cliente.mostra_informacoes()
    else:
        print("Opção inválida!")