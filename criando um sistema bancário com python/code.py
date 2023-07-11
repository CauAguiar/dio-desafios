import datetime

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.transacoes = []
        self.saldos_diarios = {}
        self.saques_diarios = {}

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


conta = ContaBancaria(1000)
conta.deposito(500)  
conta.saque(300)  
conta.saque(200)  
conta.saque(100) 
conta.saque(300)
conta.extrato() 
