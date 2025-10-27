from database import Database


def consultar_equipamentos_com_garantias():
    """
    Consulta equipamentos e suas garantias no banco de dados e imprime os resultados de forma legível.
    """
    # Estabelece a conexão com o banco de dados
    db = Database()

    # Definindo a consulta SQL que retorna equipamentos e suas garantias
    query = """
    SELECT
        e.nome AS equipamento,
        e.marca,
        e.modelo,
        e.numero_serie,
        e.preco,
        g.data_inicio,
        g.data_fim,
        g.descricao AS garantia_descricao
    FROM
        equipamento e
    JOIN
        garantia g ON e.id_equipamento = g.id_equipamento
    ORDER BY
        e.nome;
    """

    # Executando a consulta e pegando os resultados
    resultados = db.consultar(query)

    # Imprimindo os resultados de forma legível
    print("Equipamentos e Garantias:\n")
    for resultado in resultados:
        equipamento, marca, modelo, numero_serie, preco, data_inicio, data_fim, garantia_descricao = resultado
        print(f"Equipamento: {equipamento} ({marca} {modelo})")
        print(f"  Número de Série: {numero_serie}")
        print(f"  Preço: R${preco:.2f}")
        print(f"  Garantia: {garantia_descricao}")
        print(f"  Período: {data_inicio} até {data_fim}")
        print("-" * 50)

    # Fechar a conexão
    db.close()


# Executando a função no programa principal
if __name__ == "__main__":
    consultar_equipamentos_com_garantias()
