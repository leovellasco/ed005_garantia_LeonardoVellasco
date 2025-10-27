import psycopg2


class Database:
    """
    Classe responsável por gerenciar a conexão com o banco de dados PostgreSQL e realizar operações CRUD.
    """

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="app_garantia",  # Nome do banco de dados
                user="postgres",        # Usuário do banco de dados
                password="root",   # Senha do banco de dados
                host="localhost",       # Host do banco de dados
                port="5432"             # Porta do banco de dados
            )
            self.conn.autocommit = True  # Ativa o autocommit, importante para a persistência
            print("Conexão com o banco de dados estabelecida com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def consultar(self, query):
        """
        Executa uma consulta SQL no banco de dados e retorna os resultados.
        :param query: A consulta SQL a ser executada.
        :return: Resultado da consulta (uma lista de tuplas).
        """
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            resultado = cur.fetchall()
            return resultado
        except Exception as e:
            print(f"Erro na consulta: {e}")
        finally:
            cur.close()

    def executar(self, query):
        """
        Executa uma consulta SQL de alteração no banco de dados (INSERT, UPDATE, DELETE).
        :param query: A consulta SQL a ser executada.
        """
        try:
            cur = self.conn.cursor()
            cur.execute(query)
        except Exception as e:
            print(f"Erro na execução da consulta: {e}")
        finally:
            cur.close()

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        if self.conn:
            self.conn.close()
            print("Conexão com o banco de dados fechada.")
