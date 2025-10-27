class Equipamento:

    def __init__(self, id_equipamento, nome, marca, modelo, numero_serie, preco, data_aquisicao, id_loja):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.preco = preco
        self.data_aquisicao = data_aquisicao
        self.id_loja = id_loja

    def __str__(self):
        return (f"{self.nome} ({self.marca} {self.modelo}) | "
                f"Série: {self.numero_serie} | Preço: R${self.preco:.2f}")