-- Active: 1743187238197@@127.0.0.1@3306@ans_operadoras
CREATE DATABASE IF NOT EXISTS ans_operadoras;
USE ans_operadoras;

CREATE TABLE operadoras (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(18),
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(4),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(100),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    data_registro_ans DATE
);

LOAD DATA LOCAL INFILE 'relatorio\Relatorio_cadop.csv'
INTO TABLE operadoras
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
 logradouro, numero, complemento, bairro, cidade, uf, cep,
 ddd, telefone, fax, email, representante, cargo_representante,
 @data_registro_ans)
SET data_registro_ans = STR_TO_DATE(@data_registro_ans, '%d/%m/%Y');
