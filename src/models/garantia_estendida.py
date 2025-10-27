from models.garantia import Garantia

class GarantiaEstendida(Garantia):
 
    def __init__(self, id_garantia, data_inicio, data_fim, descricao, id_equipamento, provedor, cobertura_extra):
        super().__init__(id_garantia, data_inicio, data_fim, descricao, id_equipamento)
        self.provedor = provedor
        self.cobertura_extra = cobertura_extra

    def __str__(self):
        return (f"[Estendida] {super().__str__()} | Provedor: {self.provedor} | "
                f"Cobertura: {self.cobertura_extra}")