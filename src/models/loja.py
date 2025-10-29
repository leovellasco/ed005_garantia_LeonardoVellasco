class Loja:

    # Representa uma loja cadastrada no sistema.

    def __init__(self, id_loja, nome_loja, cnpj, endereco_loja=None,
                 telefone_loja=None, email_loja=None, id_usuario=None):
        self.id_loja = id_loja
        self.nome_loja = nome_loja
        self.cnpj = cnpj
        self.endereco_loja = endereco_loja
        self.telefone_loja = telefone_loja
        self.email_loja = email_loja
        self.id_usuario = id_usuario

    def __str__(self):
        return f"Loja: {self.nome_loja} (CNPJ: {self.cnpj})"
