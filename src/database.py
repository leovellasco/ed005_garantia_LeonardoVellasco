# Módulo database.py Responsável por gerenciar a conexão com o banco de dados PostgreSQL e executar consultas SQL

import psycopg2


class Database:
    """
    Classe responsável pela conexão e execução de comandos SQL no PostgreSQL.

    Métodos:
        - consultar(query): executa uma consulta SELECT e retorna os resultados.
        - executar(query, params): executa INSERT, UPDATE ou DELETE.
        - fechar_conexao(): encerra a conexão com o banco.
    """

    def __init__(self):
        """Inicializa a conexão com o banco de dados PostgreSQL."""
        try:
            self.conn = psycopg2.connect(
                dbname="app_garantia",
                user="postgres",
                password="root",
                host="localhost",
                port="5432"
            )
            print("✅ Conexão com o banco de dados estabelecida com sucesso.")
        except Exception as e:
            print("❌ Erro ao conectar ao banco de dados:", e)
            self.conn = None

    def consultar(self, query):
        """
        Executa uma consulta SELECT e retorna o resultado como lista de tuplas.
        """
        if not self.conn:
            print("Conexão não estabelecida.")
            return []

        cur = self.conn.cursor()
        try:
            cur.execute(query)
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print("❌ Erro na consulta:", e)
            return []
        finally:
            cur.close()

    def executar(self, query, params=None):
        """
        Executa comandos de modificação de dados (INSERT, UPDATE, DELETE).
        Usa commit automático para persistir as alterações.
        """
        if not self.conn:
            print("Conexão não estabelecida.")
            return

        cur = self.conn.cursor()
        try:
            cur.execute(query, params)
            self.conn.commit()
            print("✅ Comando executado com sucesso.")
        except Exception as e:
            self.conn.rollback()
            print("❌ Erro ao executar comando:", e)
        finally:
            cur.close()

    def fechar_conexao(self):
        """Fecha a conexão com o banco."""
        if self.conn:
            self.conn.close()
            print("🔒 Conexão com o banco de dados encerrada.")
