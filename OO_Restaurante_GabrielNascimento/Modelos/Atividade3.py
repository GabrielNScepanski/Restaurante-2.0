# Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f"Olá! Como vai, {self.profissao} {self.nome}?"

# Classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}"

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        self._titular = valor

# Classe ClienteBanco
class ClienteBanco:
    def __init__(self, nome, cpf, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

# Exemplo de uso das classes
# Pessoa
pessoa1 = Pessoa("João", 30, "Engenheiro")
print(pessoa1)
pessoa1.aniversario()
print(pessoa1.saudacao)

# ContaBancaria
conta1 = ContaBancaria("Maria", 1000)
conta2 = ContaBancaria("José", 2000)
print(conta1)
print(conta2)
ContaBancaria.ativar_conta(conta1)
print(f"A conta de {conta1.titular} está ativa? {conta1.ativo}")

# ClienteBanco
cliente1 = ClienteBanco("Ana", "123.456.789-00", "Rua A, 123", "(41) 1234-5678", "ana@email.com")
cliente2 = ClienteBanco("Pedro", "987.654.321-00", "Rua B, 456", "(41) 8765-4321", "pedro@email.com")
cliente3 = ClienteBanco("Carla", "456.123.789-00", "Rua C, 789", "(41) 5678-1234", "carla@email.com")
