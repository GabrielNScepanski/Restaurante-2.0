# Classe Carro
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

# Classe Restaurante
class Restaurante:
    def __init__(self, nome, categoria, especialidade='Comida Caseira', faixa_preco='R$20 a R$40'):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.especialidade = especialidade
        self.faixa_preco = faixa_preco

    def __str__(self):
        return f'Restaurante {self.nome}, Categoria: {self.categoria}'

# Classe Cliente
class Cliente:
    def __init__(self, nome, idade, email, endereco):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.endereco = endereco

# Instanciando a classe Carro
meu_carro = Carro('Fusca', 'Azul', 1969)

# Instanciando a classe Restaurante
meu_restaurante = Restaurante('Sabor da Terra', 'Brasileira', 'Churrasco', 'R$30 a R$50')
novo_restaurante = Restaurante('Delícias do Campo', 'Vegetariana')

# Instanciando objetos da classe Cliente
cliente1 = Cliente('Ana', 32, 'ana@email.com', 'Rua das Flores, 123')
cliente2 = Cliente('Carlos', 45, 'carlos@email.com', 'Avenida Brasil, 456')
cliente3 = Cliente('Beatriz', 28, 'beatriz@email.com', 'Alameda dos Anjos, 789')

# Testando o método __str__ da classe Restaurante
print(novo_restaurante)

