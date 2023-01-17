from mimetypes import init


class Conta:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def mostrar_informacoes(self):
        print("DADOS DA CONTA: ")
        print(f"Correntista: {self.nome}")
        print(f"CPF: {self.cpf}")
        self.mostrar_saldo()
            
    def mostrar_saldo(self):
       print(f"Saldo: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def transferir(self, destino, valor):
       if self.sacar(valor):
           destino.depositar(valor)
           print("Transferência efetuada")
           return True
       else:
           return False    


class ContaEspecial(Conta):
    
    def __init__(self, nome, cpf, limite):
        super().__init__(nome, cpf)
        self.limite = limite

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        self.mostrar_limite()

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        else:
            print("Impossível sacar")
            return False

    def mostrar_limite(self):
        print(f'Limite Disponível: {self.saldo + self.limite}')

