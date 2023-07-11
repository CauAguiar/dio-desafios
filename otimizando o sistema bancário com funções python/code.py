import datetime

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    numero_conta = 1
    agencia = "0001"

    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0
        self.transacoes = []
        self.saldos_diarios = {}
        self.saques_diarios = {}
        self.numero_conta = ContaCorrente.numero_conta
        ContaCorrente.numero_conta += 1

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(("Depósito", valor))
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
        if self.saldo <= 0:
            print("Saldo insuficiente para realizar o saque.")
            return

        hoje = datetime.date.today()
        if hoje not in self.saques_diarios:
            self.saques_diarios[hoje] = 0
        else:
            if self.saques_diarios[hoje] >= 3:
                print("Limite máximo de saques diários atingido.")
                return

        if valor <= self.saldo and valor <= 500:
            self.saldo -= valor
            self.transacoes.append(("Saque", valor))
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
            self.saques_diarios[hoje] += 1
        else:
            print("Valor de saque inválido.")

    def extrato(self):
        print("----- Extrato -----")
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.transacoes:
                tipo, valor = transacao
                print(f"{tipo}: R${valor:.2f}")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("-------------------")

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (DD-MM-AAAA): ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço: ")

    # Verificar se o CPF já está registrado
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Já existe um usuário com esse CPF.")
            return None

    # Criar uma instância de Usuario e adicioná-la à lista de usuários
    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)
    return usuario

def cadastrar_conta_corrente(usuario):
    # Criar uma instância de ContaCorrente vinculada ao usuário
    conta_corrente = ContaCorrente(usuario)
    contas_correntes.append(conta_corrente)
    return conta_corrente

def exibir_menu():
    print("----- Menu -----")
    print("1. Cadastrar usuário")
    print("2. Cadastrar conta corrente")
    print("3. Fazer depósito")
    print("4. Fazer saque")
    print("5. Ver extrato")
    print("0. Sair")

usuarios = []
contas_correntes = []

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        usuario = cadastrar_usuario()
        if usuario:
            print("Usuário cadastrado com sucesso.")
        else:
            print("Falha ao cadastrar usuário.")
    elif opcao == "2":
        cpf = input("Digite o CPF do usuário para vincular a conta corrente: ")
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.cpf == cpf:
                usuario_encontrado = usuario
                break
        if usuario_encontrado:
            conta_corrente = cadastrar_conta_corrente(usuario_encontrado)
            print(f"Conta corrente criada: Agência: {conta_corrente.agencia}, Número: {conta_corrente.numero_conta}")
        else:
            print("Usuário não encontrado.")
    elif opcao == "3":
        cpf = input("Digite o CPF do usuário para fazer o depósito: ")
        valor = float(input("Digite o valor do depósito: "))
    
        conta_encontrada = None
        for conta in contas_correntes:
            if conta.usuario.cpf == cpf:
                conta_encontrada = conta
                break
        
        if conta_encontrada:
            conta_encontrada.deposito(valor)
        else:
            print("Usuário não encontrado.")
    
    elif opcao == "4":
        cpf = input("Digite o CPF do usuário para fazer o saque: ")
        valor = float(input("Digite o valor do saque: "))
    
        conta_encontrada = None
        for conta in contas_correntes:
            if conta.usuario.cpf == cpf:
                conta_encontrada = conta
                break
        
        if conta_encontrada:
            conta_encontrada.saque(valor)
        else:
            print("Usuário não encontrado.")
    
    elif opcao == "5":
        cpf = input("Digite o CPF do usuário para ver o extrato: ")
    
        conta_encontrada = None
        for conta in contas_correntes:
            if conta.usuario.cpf == cpf:
                conta_encontrada = conta
                break
        
        if conta_encontrada:
            conta_encontrada.extrato()
        else:
            print("Usuário não encontrado.")
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Digite novamente.")
