class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): # -> serve para exibir em formato de texto
        return self._nome
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'| {'ID':^10} | {'Restaurante':^35} | {'Categoria':^35} | {'Status':^15} |' )
        for id, restaurante in enumerate(cls.restaurantes):
            print(f'| {id:^10} | {restaurante._nome:^35} | {restaurante._categoria:^35} | {restaurante.ativo:^15} |')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

    def alterar_status(self):
        self._ativo = not self._ativo

restaurante_cordoba = Restaurante('Restaurante Cordoba', 'Argentina')

Restaurante.listar_restaurantes()


