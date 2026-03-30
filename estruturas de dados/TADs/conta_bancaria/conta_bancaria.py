class ContaBancaria:
    def __init__(self, numero_conta, titular):
        self.saldo = 0
        self.numero_conta = numero_conta
        self.titular = titular
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        valor_novo = self.saldo - valor
        if valor_novo <= 0:
            print('Saldo insuficiente para essa operação.')
            return
        self.saldo = valor_novo

    def ver_saldo(self):
        print(f'Saldo da conta: {self.saldo}')
