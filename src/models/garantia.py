from datetime import date

class Garantia:

    # Representa uma garantia de equipamento.

    def __init__(self, id_garantia, data_inicio, data_fim, tipo_garantia,
                 id_equip=None, id_usuario=None):
        self.id_garantia = id_garantia
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.tipo_garantia = tipo_garantia
        self.id_equip = id_equip
        self.id_usuario = id_usuario

    def __str__(self):
        dias_restantes = (self.data_fim - date.today()).days
        return f"Garantia {self.tipo_garantia} - vence em {self.data_fim} ({dias_restantes} dias restantes)"

class GarantiaEstendida(Garantia):
    """
    Representa uma garantia estendida, herdando de Garantia.

    Atributos adicionais:
        empresa_responsavel (str): Nome da empresa que oferece a garantia estendida.
        custo_adicional (float): Valor pago pela extensão da garantia.
    """

    def __init__(self, id_garantia, data_inicio, data_fim, id_equip,
                 id_usuario, empresa_responsavel, custo_adicional):
        super().__init__(id_garantia, data_inicio,
                         data_fim, 'estendida', id_equip, id_usuario)
        self.empresa_responsavel = empresa_responsavel
        self.custo_adicional = custo_adicional

    def __str__(self):
        return (f"Garantia Estendida ({self.empresa_responsavel}) "
                f"- Válida até {self.data_fim} - Custo adicional: R${self.custo_adicional:.2f}")

