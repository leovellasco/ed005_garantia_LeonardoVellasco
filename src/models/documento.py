class Documento:

    # Representa um documento vinculado a uma loja, equipamento ou garantia.

    def __init__(self, id_documento, url, tipo_doc, num_doc=None,
                 data_emissao=None, id_loja=None, id_equip=None, id_garantia=None):
        self.id_documento = id_documento
        self.url = url
        self.tipo_doc = tipo_doc
        self.num_doc = num_doc
        self.data_emissao = data_emissao
        self.id_loja = id_loja
        self.id_equip = id_equip
        self.id_garantia = id_garantia

    def __str__(self):
        return f"Documento {self.tipo_doc.upper()} ({self.num_doc}) - Emitido em {self.data_emissao}"
