class Equipamento:

    # Representa um equipamento vinculado a uma loja.

    def __init__(self, id_equip, nome_equip, data_aquisicao, marca=None,
                 modelo=None, numero_serie=None, preco=None, id_loja=None, id_usuario=None):
        self.id_equip = id_equip
        self.nome_equip = nome_equip
        self.data_aquisicao = data_aquisicao
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.preco = preco
        self.id_loja = id_loja
        self.id_usuario = id_usuario

    def __str__(self):
        return f"{self.nome_equip} ({self.marca} {self.modelo}) - Nº Série: {self.numero_serie}"
