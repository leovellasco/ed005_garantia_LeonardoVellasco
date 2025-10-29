-- =========================================================
-- INSERÇÕES NA TABELA: usuario
-- =========================================================

INSERT INTO usuario (nome_usuario, cpf, email_usuario, telefone_usuario, senha)
VALUES
('Ana Souza', '12345678901', 'ana.souza@example.com', '(11)98888-1111', 'senha123'),
('Bruno Lima', '23456789012', 'bruno.lima@example.com', '(21)97777-2222', 'senha456'),
('Carla Mendes', '34567890123', 'carla.mendes@example.com', '(31)96666-3333', 'senha789');

-- =========================================================
-- INSERÇÕES NA TABELA: loja
-- =========================================================

INSERT INTO loja (nome_loja, cnpj, endereco_loja, telefone_loja, email_loja, id_usuario)
VALUES
('TechStore', '12345678000199', 'Av. Paulista, 1000 - São Paulo/SP', '(11)4002-8922', 'contato@techstore.com', 1),
('Eletrônicos BR', '98765432000155', 'Rua das Flores, 200 - Rio de Janeiro/RJ', '(21)3003-4455', 'vendas@eletronicosbr.com', 2),
('MegaCell', '45678912000133', 'Av. Afonso Pena, 500 - Belo Horizonte/MG', '(31)3555-9090', 'suporte@megacell.com', 3);

-- =========================================================
-- INSERÇÕES NA TABELA: equipamentos
-- =========================================================

INSERT INTO equipamentos (nome_equip, data_aquisicao, marca, modelo, numero_serie, preco, id_loja, id_usuario)
VALUES
('Notebook Dell Inspiron 15', '2023-01-15', 'Dell', 'Inspiron 15 3000', 'SN123456', 3500.00, 1, 1),
('Smartphone Samsung Galaxy S22', '2023-03-10', 'Samsung', 'Galaxy S22', 'SN987654', 4200.00, 2, 2),
('Impressora HP LaserJet 1020', '2023-05-25', 'HP', 'LaserJet 1020', 'SN567890', 900.00, 3, 3);
-- =========================================================
-- INSERÇÕES NA TABELA: garantia
-- =========================================================

INSERT INTO garantia (data_inicio, data_fim, tipo_garantia, id_equip, id_usuario)
VALUES
('2023-01-15', '2025-01-15', 'fabricante', 1, 1),
('2023-03-10', '2024-03-10', 'estendida', 2, 2),
('2023-05-25', '2024-05-25', 'loja', 3, 3);

-- =========================================================
-- INSERÇÕES NA TABELA: documento
-- =========================================================

INSERT INTO documento (url, tipo_doc, num_doc, data_emissao, id_loja, id_equip, id_garantia)
VALUES
('https://docs.techstore.com/notafiscal123.pdf', 'nota_fiscal', 'NF123', '2023-01-15', 1, 1, 1),
('https://docs.eletronicosbr.com/certificado_s22.pdf', 'certificado', 'CERT987', '2023-03-10', 2, 2, 2),
('https://docs.megacell.com/manual_hp1020.pdf', 'outro', 'DOC567', '2023-05-25', 3, 3, 3);
