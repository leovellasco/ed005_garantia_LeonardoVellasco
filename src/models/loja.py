class Loja:

    def __init__(self, id_loja, nome, cnpj, endereco, telefone, email):
        self.id_loja = id_loja
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Loja: {self.nome} | CNPJ: {self.cnpj} | Email: {self.email}"