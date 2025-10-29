# Documentação README - Estudo Dirigido 005 - Banco de Dados e POO


## Entidades principais da aplicação: Usuário, Loja, Equipamento, Garantia e Documento.

As cinco entidades principais da aplicação são:

**Usuário**: Representa o dono da conta que utiliza o sistema.
Cada usuário pode cadastrar lojas, equipamentos, garantias e documentos.
________________________________________
**Loja**: Armazena as informações sobre o estabelecimento onde o equipamento foi adquirido.
Cada loja pertence a um usuário e pode ter vários equipamentos e documentos vinculados.
________________________________________
**Equipamento**: Representa um produto comprado pelo usuário, que terá documentos e garantias associadas.
________________________________________
**Garantia**: Contém os dados sobre a cobertura de um equipamento — seja de fabricante, estendida ou da loja.
Cada garantia está vinculada a um equipamento e ao usuário.
________________________________________
**Documento**: Registra os arquivos digitais (nota fiscal, certificado, comprovante etc.) que comprovam a compra ou o vínculo da garantia.
Pode estar ligado a uma loja, equipamento e/ou garantia.

## Atributos de cada entidade e justificativa de uso

### Entidade Usuário
---
```
Atributo             Tipo de dado       Justificativa

id_usuario	         SERIAL (PK)	    Identificador único do usuário.
nome_usuario	     VARCHAR(100)	    Nome completo do usuário.
cpf	                 CHAR(11)	        Identificação única no sistema.
email_usuario	     VARCHAR(150)	    Canal principal de contato e login.
telefone_usuario	 VARCHAR(20)	    Contato alternativo.
status	             VARCHAR(10)	    Indica se o usuário está ativo ou inativo.
senha	             VARCHAR(255)	    Armazena a senha criptografada.
```
### Entidade Loja	
---   
```  
Atributo            Tipo de dado        Justificativa	 

id_loja	            SERIAL (PK)	        Identificador único da loja.
nome_loja	        VARCHAR(100)	    Nome do estabelecimento.
cnpj	            CHAR(14)	        Identificação fiscal única.
endereco_loja	    VARCHAR(200)	    Endereço físico da loja.
telefone_loja   	VARCHAR(20)	        Contato comercial.
email_loja	        VARCHAR(150)	    Comunicação eletrônica.
id_usuario	        INT (FK)	        Liga a loja ao usuário responsável.
```

### Entidade Equipamento
---	  
```     
Atributo            Tipo de dado        Justificativa

id_equip        	SERIAL (PK)	        Identificador único do equipamento.
nome_equip	        VARCHAR(100)	    Nome ou descrição do equipamento.
data_aquisicao	    DATE	            Data de compra.
marca	            VARCHAR(50)     	Marca do produto.
modelo	            VARCHAR(50)	        Modelo do produto.
numero_serie	    VARCHAR(100)	    Número de série, usado para rastreamento.
preco	            NUMERIC(10,2)	    Valor de compra.
id_loja	            INT (FK)	        Loja onde foi comprado.
id_usuario	        INT (FK)	        Dono do equipamento.
```

### Entidade Garantia	
---   
```  
Atributo            Tipo de dado        Justificativa

id_garantia	        SERIAL (PK)	        Identificador único da garantia.
data_inicio	        DATE	            Início da validade da garantia.
data_fim	        DATE	            Fim da cobertura.
tipo_garantia	    VARCHAR(20)	        Classifica a garantia (fabricante, loja, estendida).
id_equip	        INT (FK)	        Equipamento vinculado.
id_usuario	        INT (FK)	        Usuário responsável.
```
### Entidade Documento	
--- 
```
Atributo            Tipo de dado        Justificativa

id_documento	    SERIAL (PK)	        Identificador único do documento.
url	                VARCHAR(255)	    Caminho ou link para o arquivo.
tipo_doc	        VARCHAR(20)	        Tipo de documento (nota fiscal, certificado, outro).
num_doc	            VARCHAR(50)	        Número de controle (ex: número da nota).
data_emissao	    DATE	            Data de emissão do documento.
id_loja	            INT (FK, opcional)	Loja relacionada.
id_equip	        INT (FK, opcional)	Equipamento vinculado.
id_garantia     	INT (FK, opcional)	Garantia vinculada.
```

## Chaves primárias e estrangeiras.
```
Entidade	         PK	           FKs	                             Relaciona-se com

usuario	        id_usuario      	—                        	            —
loja	        id_loja	        id_usuario	                         usuario(id_usuario)
equipamento     id_equip	    id_loja, id_usuario	                 loja(id_loja), usuario(id_usuario)
garantia     	id_garantia	    id_equip, id_usuario                 equipamento(id_equip), usuario(id_usuario)
documento	    id_documento	id_loja, id_equip, id_garantia	     loja, equipamento, garantia
```

## Justificativa técnica para as relações criadas 

    •	Usuário x Loja (1:N): 
    Um usuário pode cadastrar várias lojas (onde fez compras), mas cada loja pertence a um único usuário.

    •	Usuário x Equipamento (1:N)
    Um usuário pode ter vários equipamentos, mas cada equipamento pertence a apenas um usuário.

    •	Loja x Equipamento (1:N)
    Uma loja pode vender muitos equipamentos, mas cada equipamento é comprado em uma loja.

    •	Equipamento x Garantia (1:N)
    Um equipamento pode ter várias garantias (por exemplo, do fabricante e uma estendida), mas cada garantia pertence a apenas um equipamento.

    •	Equipamento x Documento (1:N)
    Um equipamento pode possuir diversos documentos (nota fiscal, certificado etc.), mas cada documento se refere a um único equipamento.

    •	Garantia x Documento (1:N)
    Uma garantia pode ter mais de um documento associado (certificados, comprovantes), mas cada documento está vinculado a uma única garantia.

    •	Usuário x Garantia (1:N)
    Cada garantia pertence ao usuário que registrou o equipamento, garantindo integridade dos dados.
    Reflexão: explique a diferença entre modelo conceitual, lógico e físico. 

## Consultas:

### Quais equipamentos estão vinculados a cada loja?
```
SELECT
    l.id_loja,
    l.nome_loja,
    e.id_equip,
    e.nome_equip,
    e.marca,
    e.modelo,
    e.data_aquisicao
FROM loja l
JOIN equipamentos e ON l.id_loja = e.id_loja
ORDER BY l.nome_loja, e.nome_equip;
```
    Explicação: Esta consulta faz um join entre loja e equipamentos, listando todos os equipamentos pertencentes a cada loja. O ORDER BY organiza os resultados primeiro pelo nome da loja e depois pelo nome do equipamento.

    Uso na aplicação:
    •	Exibir no painel administrativo a lista de equipamentos por loja.
    •	Gerar relatórios de inventário por unidade.
    •	Ajudar na gestão de ativos, especialmente quando há múltiplas filiais.

### Quais garantias vencem nos próximos 30 dias?
```
SELECT
    g.id_garantia,
    e.nome_equip,
    l.nome_loja,
    g.data_fim AS data_vencimento,
    g.tipo_garantia
FROM garantia g
JOIN equipamentos e ON g.id_equip = e.id_equip
JOIN loja l ON e.id_loja = l.id_loja
WHERE g.data_fim BETWEEN CURRENT_DATE AND (CURRENT_DATE + INTERVAL '30 days')
ORDER BY g.data_fim;
```
    Explicação:
    Filtra todas as garantias cujo término (data_fim) ocorrerá dentro dos próximos 30 dias a partir da data atual.

    Uso na aplicação:
    •	Geração de alertas automáticos para o time de suporte ou manutenção.
    •	Exibição em um dashboard de notificações para que a equipe possa agir preventivamente.
    •	Envio de emails ou notificações push para usuários responsáveis.

### Qual loja possui o maior número de garantias vencidas?
```
SELECT
    l.id_loja,
    l.nome_loja,
    COUNT(g.id_garantia) AS qtd_garantias_vencidas
FROM loja l
JOIN equipamentos e ON l.id_loja = e.id_loja
JOIN garantia g ON e.id_equip = g.id_equip
WHERE g.data_fim < CURRENT_DATE
GROUP BY l.id_loja, l.nome_loja
ORDER BY qtd_garantias_vencidas DESC
LIMIT 1;
```
    Explicação:
    Conta quantas garantias já estão vencidas (data_fim < CURRENT_DATE) por loja, e retorna aquela com o maior número de garantias expiradas.

    Uso na aplicação:
    •	Exibir em relatórios gerenciais quais filiais estão com mais garantias expiradas (indicando possíveis riscos de custo de manutenção).
    •	Ajudar a priorizar renovações ou ações corretivas.
    •	Geração de indicadores de desempenho (KPIs) por loja.

### Qual o tempo médio de garantia por loja?
```
SELECT
    l.id_loja,
    l.nome_loja,
    ROUND(AVG(g.data_fim - g.data_inicio)) AS media_dias_garantia
FROM loja l
JOIN equipamentos e ON l.id_loja = e.id_loja
JOIN garantia g ON e.id_equip = g.id_equip
GROUP BY l.id_loja, l.nome_loja
ORDER BY media_dias_garantia DESC;
```
    Explicação:
    Calcula a média de duração das garantias (em dias) por loja.
    O cálculo é feito pela diferença entre data_fim e data_inicio, e o AVG() retorna a média de todas as garantias daquela loja.

    Uso na aplicação:
    •	Geração de relatórios analíticos sobre o comportamento de compras e fornecedores.
    •	Avaliar se determinadas lojas costumam ter garantias mais curtas (pode indicar contratos piores ou produtos de menor durabilidade).
    •	Apoiar negociações futuras com fornecedores.


## Reflexão pessoal:

### O que aprendi neste estudo?

    Neste exercício, aprendi a:
    •	Utilizar PostgreSQL com Python para persistir dados e consultar informações de um banco de dados.
    •	Criar classes em Python para modelar entidades do banco de dados (POO), representando tabelas como objetos.
    •	Trabalhar com a biblioteca psycopg2, utilizando-a para interagir com um banco de dados PostgreSQL.
    •	Estruturar um código modular com camadas bem definidas (conexão, consulta, e processamento de dados).


### Que erros enfrentei e como resolvi?

    •	Erros na integração do PostgreSQL com o DBeaver: Tive que dar uma pesquisada pois estava acontecendo alguns erros na hora da execução do Banco de Dados
    •	Erro na instalação do psycopg2: Tive problemas com a instalação do pacote psycopg2, que não estava sendo encontrado no meu ambiente Python. Resolvi isso com a instalação do psycopg2

### Como este exercício se conecta ao projeto integrador?

    Este exercício está diretamente relacionado ao meu projeto integrador, pois ele aborda a persistência de dados e a interação com bancos de dados, que é uma das funcionalidades essenciais para o projeto. A implementação de um sistema que armazena e consulta dados de maneira eficiente é uma parte fundamental do desenvolvimento de sistemas de gestão ou controle, como o que estamos pensando em criar no Projeto Integrador. Além disso, o conceito de camadas (modelagem, persistência e execução) e o uso de boas práticas de POO são fundamentais para garantir que o projeto seja escalável e bem estruturado.




