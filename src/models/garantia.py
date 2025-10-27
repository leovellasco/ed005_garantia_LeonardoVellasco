class Garantia:

    def __init__(self, id_garantia, data_inicio, data_fim, descricao, id_equipamento):
        self.id_garantia = id_garantia
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.descricao = descricao
        self.id_equipamento = id_equipamento

    def __str__(self):
        return f"Garantia de {self.data_inicio} a {self.data_fim} | {self.descricao}"