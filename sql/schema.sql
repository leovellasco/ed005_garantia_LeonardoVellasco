CREATE DATABASE app_garantia;

-- =========================================================
-- TABELA: usuario
-- =========================================================

CREATE TABLE usuario (
    id_usuario      SERIAL PRIMARY KEY,
    nome_usuario    VARCHAR(100) NOT NULL,
    cpf             CHAR(11) UNIQUE NOT NULL,
    email_usuario   VARCHAR(150) UNIQUE NOT NULL,
    telefone_usuario VARCHAR(20),
    status          VARCHAR(10) DEFAULT 'ativo' CHECK (status IN ('ativo', 'inativo')),
    senha           VARCHAR(255) NOT NULL,
    data_cadastro   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- TABELA: loja
-- =========================================================

CREATE TABLE loja (
    id_loja         SERIAL PRIMARY KEY,
    nome_loja       VARCHAR(100) NOT NULL,
    cnpj            CHAR(14) UNIQUE NOT NULL,
    endereco_loja   VARCHAR(200),
    telefone_loja   VARCHAR(20),
    email_loja      VARCHAR(150),
    id_usuario      INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================================================
-- TABELA: equipamentos
-- =========================================================

CREATE TABLE equipamentos (
    id_equip        SERIAL PRIMARY KEY,
    nome_equip      VARCHAR(100) NOT NULL,
    data_aquisicao  DATE NOT NULL,
    marca           VARCHAR(50),
    modelo          VARCHAR(50),
    numero_serie    VARCHAR(100) UNIQUE,
    preco           NUMERIC(10,2),
    id_loja         INT NOT NULL,
    id_usuario      INT NOT NULL,
    FOREIGN KEY (id_loja) REFERENCES loja(id_loja)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================================================
-- TABELA: garantia
-- =========================================================

CREATE TABLE garantia (
    id_garantia     SERIAL PRIMARY KEY,
    data_inicio     DATE NOT NULL,
    data_fim        DATE NOT NULL,
    tipo_garantia   VARCHAR(20) NOT NULL CHECK (tipo_garantia IN ('fabricante', 'estendida', 'loja')),
    id_equip        INT NOT NULL,
    id_usuario      INT NOT NULL,
    FOREIGN KEY (id_equip) REFERENCES equipamentos(id_equip)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================================================
-- TABELA: documento
-- =========================================================
CREATE TABLE documento (
    id_documento    SERIAL PRIMARY KEY,
    url             VARCHAR(255) NOT NULL,
    tipo_doc        VARCHAR(20) NOT NULL CHECK (tipo_doc IN ('nota_fiscal', 'certificado', 'outro')),
    num_doc         VARCHAR(50),
    data_emissao    DATE,
    id_loja         INT,
    id_equip        INT,
    id_garantia     INT,
    FOREIGN KEY (id_loja) REFERENCES loja(id_loja)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (id_equip) REFERENCES equipamentos(id_equip)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (id_garantia) REFERENCES garantia(id_garantia)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

