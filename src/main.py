# Módulo principal da aplicação - Demonstra o uso da classe Database para consultar dados do banco e exibir informações

from database import Database


def main():
    # Instancia o objeto de conexão
    db = Database()

    # Consulta: equipamentos e suas garantias associadas
    query = """
        SELECT 
            e.id_equip,
            e.nome_equip,
            e.marca,
            e.modelo,
            g.id_garantia,
            g.tipo_garantia,
            g.data_inicio,
            g.data_fim
        FROM equipamentos e
        JOIN garantia g ON e.id_equip = g.id_equip
        ORDER BY e.nome_equip;
    """

    resultados = db.consultar(query)

    # Exibição dos resultados
    print("\n=== 📋 Lista de Equipamentos e Garantias ===")
    if not resultados:
        print("Nenhum registro encontrado.")
    else:
        for row in resultados:
            id_equip, nome, marca, modelo, id_gar, tipo, inicio, fim = row
            print(f"""
----------------------------------------
Equipamento: {nome} ({marca} {modelo})
ID Equip: {id_equip}
Garantia: {tipo} (ID: {id_gar})
Início: {inicio} | Fim: {fim}
""")

    # Fecha conexão ao final
    db.fechar_conexao()


if __name__ == "__main__":
    main()
