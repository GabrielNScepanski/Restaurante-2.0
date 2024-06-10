class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {"Ativo" if self._ativo else "Inativo"}'

    @classmethod
    def listar_restaurantes(cls):
        print("Nome do restaurante".ljust(20) + "|" + "Categoria".ljust(20) + "|" + "Status".ljust(20))
        for restaurante in cls.restaurantes:
            status = "☐" if not restaurante._ativo else "☒"
            print(f'{restaurante.nome.ljust(20)}|{restaurante.categoria.ljust(20)}|{status}')


restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante2 = Restaurante('Pizza Express', 'Italiana')


restaurante1._ativo = True


Restaurante.listar_restaurantes()

