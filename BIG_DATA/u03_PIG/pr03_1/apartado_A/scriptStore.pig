-- Cargar datos dese el archivo, todos los usuarios
usuarios = LOAD 'pr03_1/u.user' USING PigStorage('|') AS (cod:int,edad:int,genero:chararray,rol:chararray,cp:chararray);

-- 1. Muestra el total de hombres y mujeres que hay en el archivo u.user. 
-- Agrupar registros por genero (M y F)
generos = GROUP usuarios BY genero;  
   
-- Proyección realizando un conteo total de cada grupo
totalGeneros = FOREACH generos GENERATE group, COUNT(usuarios);

-- Mostrar resultado
dump totalGeneros;

-- Guardar resultado
STORE totalGeneros INTO 'pig_usuarios/totalGeneros' USING PigStorage(',');


-- -----------


-- 2. Mediante instrucciones de PIG encontrar las 10 ocupaciones más frecuentes entre los usuarios.
-- *A partir de ahora, se sobre entiende que el archivo ya estar cargado en usuarios

-- Agrupar por rol (ocupación)
roles= GROUP usuarios BY rol;

-- Contar el total de cada rol
totalRoles = FOREACH roles GENERATE group, COUNT(usuarios) AS total;

-- Ordenar de forma descendente los roles más repetidos
ordenarRoles = ORDER totalRoles BY total DESC;

-- Limitar el listado a las 10 primeras posiciones de los roles más habituales
topRoles = LIMIT ordenarRoles 10;

-- Mostrar resultado
dump topRoles;

-- Guardar resultado
STORE topRoles INTO 'pig_usuarios/topRoles' USING PigStorage(',');


-- -----------


-- 3. Muestra la edad media por géneros.

-- Agrupar por géneros
generos = GROUP usuarios BY genero;

-- Calcular edad media de cada género
mediaGeneros = FOREACH generos GENERATE group, AVG(usuarios.edad);

-- Mostrar resultado
dump mediaGeneros;

-- Guardar resultado
STORE mediaGeneros INTO 'pig_usuarios/mediaGeneros' USING PigStorage(',');


-- -----------


-- 4. Muestra la edad media por ocupaciones. 

-- Agrupar por rol (ocupación)
roles= GROUP usuarios BY rol;

-- Calcular edad media por rol
mediaRoles = FOREACH roles GENERATE group, AVG(usuarios.edad);

-- Mostrar resultado
dump mediaRoles;

-- Guardar resultado
STORE mediaRoles INTO 'pig_usuarios/mediaRoles' USING PigStorage(',');
