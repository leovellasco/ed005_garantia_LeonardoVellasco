class Usuario:

    # Representa um usuário do sistema.

    def __init__(self, id_usuario, nome_usuario, cpf, email_usuario,
                 telefone_usuario=None, status='ativo', senha=None, data_cadastro=None):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.cpf = cpf
        self.email_usuario = email_usuario
        self.telefone_usuario = telefone_usuario
        self.status = status
        self.senha = senha
        self.data_cadastro = data_cadastro

    def __str__(self):
        return f"Usuário: {self.nome_usuario} ({self.email_usuario}) - Status: {self.status}"
