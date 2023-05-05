SELECT *
FROM vinhos --SELEÇÃO DE TODOS OS REGISTROS

SELECT *
FROM vinhos
WHERE PREÇO BETWEEN '0' AND '50'
ORDER BY PREÇO ASC --SELEÇÃO DE PRODUTOS DE R$0,00 Á R$50,00 EM ORDEM CRESCENTE DOS PREÇOS

SELECT * 
FROM vinhos 
WHERE PREÇO BETWEEN '50' AND '300'
ORDER BY PREÇO ASC  --SELEÇÃO DE PRODUTOS DE R$50,00 Á R$300,00 EM ORDEM CRESCENTE DOS PREÇOS

SELECT *, COUNT(PREÇO) AS QTD_PREÇO
FROM vinhos
WHERE PREÇO > '0'
GROUP BY PREÇO
HAVING COUNT(PREÇO)
ORDER BY MARCA --SELEÇÃO DE PRODUTOS E A CONTAGEM DOS 
			   --PREÇOS DE CADA PRODUTO, AGRUPANDO AS CONTAGENS E ORDENANDO
			   
DELETE FROM vinhos --EXCLUSÃO DE TODOS OS REGISTROS DA TABELA

INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('2', 'DFJ Vinhos', '59.9', 'Branco');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('3', 'DFJ Vinhos', '69.9', 'Branco');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('5', 'DFJ Vinhos', '69.9', 'Rosé');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('6', 'DFJ Vinhos', '59.9', 'Rosé');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('7', 'DFJ Vinhos', '69.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('8', 'DFJ Vinhos', '99.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('9', 'J. García Carrión', '29.9', 'Rosé');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('10', 'J. García Carrión', '32.9', 'Rosé');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('11', 'J. García Carrión', '39.9', 'Branco');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('12', 'J. García Carrión', '29.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('14', 'J. García Carrión', '36.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('15', 'J. García Carrión', '39.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('17', 'Fecovita', '49.9', 'Branco');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('18', 'Fecovita', '39.9', 'Branco');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('20', 'Fecovita', '29.9', 'Rosé');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('21', 'Fecovita', '39.9', 'Rosé');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('22', 'Fecovita', '36.9', 'Rosé');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('25', 'Fecovita', '39.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('31', 'Fecovita', '29.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('32', 'Fecovita', '34.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('34', 'Fecovita', '36.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('35', 'Fecovita', '79.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('36', 'Fecovita', '109.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('37', 'Bodegas y Viñedos Baudron', '26.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('38', 'Bodegas y Viñedos Baudron', '39.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('39', 'Bodega Del Fin Del Mundo', '109.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('40', 'Bodega Del Fin Del Mundo', '259.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('41', 'Bodega Del Fin Del Mundo', '109.9', 'Branco');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('42', 'Bodega Del Fin Del Mundo', '89.9', 'Rosé');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('43', 'Andean Vineyards', '34.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('45', 'Belhara Estate', '27.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('46', 'Belhara Estate', '44.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('48', 'Belhara Estate', '159.6', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('49', 'Belhara Estate', '39.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('51', 'Casa Perini', '64.9', 'Tinto');
INSERT INTO vinhos ("ID", "MARCA", "PREÇO", "TIPO") VALUES ('52', 'Fecovita', '100.0', 'Gourmet');