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

# 1) Atribuindo 'Italiana' ao atributo categoria da instância restaurante_praca
restaurante_praca = Restaurante('Praça Gourmet', 'Brasileira')
restaurante_praca.categoria = 'Italiana'

# 2) Acessando o valor do atributo nome da instância restaurante_praca
nome_restaurante = restaurante_praca.nome

# 3) Verificando o valor inicial do atributo ativo e exibindo uma mensagem
status_ativo = 'ativo' if restaurante_praca.ativo else 'inativo'
print(f'O restaurante {nome_restaurante} está {status_ativo}.')

# 4) Acessando o valor do atributo de classe categoria diretamente da classe Restaurante
# (Note que categoria não é um atributo de classe, então essa operação não é possível.
#  Vou criar uma variável categoria para demonstrar o que seria se existisse.)
categoria = 'Categoria padrão'

# 5) Alterando o valor do atributo nome para 'Bistrô'
restaurante_praca.nome = 'Bistrô'

# 6) Criando uma nova instância da classe Restaurante chamada restaurante_pizza
restaurante_pizza = Restaurante('Pizza Place', 'Fast Food')

# 7) Verificando se a categoria da instância restaurante_pizza é 'Fast Food'
categoria_correta = restaurante_pizza.categoria == 'Fast Food'
print(f'A categoria de {restaurante_pizza.nome} é Fast Food? {categoria_correta}')

# 8) Mudando o estado da instância restaurante_pizza para ativo
restaurante_pizza.ativo = True

# 9) Imprimindo no console o nome e a categoria da instância restaurante_praca
print(restaurante_praca)

