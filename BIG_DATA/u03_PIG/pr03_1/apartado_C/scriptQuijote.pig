-- CARGAR
quijote = LOAD 'pr03_1/quijote.txt' AS (linea:chararray);

-- TOKENIZE
lineasToken = FOREACH quijote GENERATE TOKENIZE(linea) AS tokensCol;

-- FLATTEN
palabraXlinea = FOREACH lineasToken GENERATE FLATTEN(tokensCol) AS palabra;

-- GROUP
palabraXlineaGrupo = GROUP palabraXlinea BY palabra;

-- COUNT
totalPalabras = FOREACH palabraXlineaGrupo GENERATE group AS palabra, COUNT(palabraXlinea) AS cantidad;

-- ORDENAR
totalPalabrasOrder = ORDER totalPalabras BY cantidad DESC;

-- STORE
STORE totalPalabrasOrder INTO 'pig_quijote' USING PigStorage(',');
