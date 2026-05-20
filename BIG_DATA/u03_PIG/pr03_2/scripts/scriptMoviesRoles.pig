-- LOAD votaciones
votes = LOAD 'pr03_2/u.data' USING PigStorage('\t') AS (userId:chararray,movieId:chararray,rating:double);

-- LOAD movies
movies = LOAD 'pr03_2/u.item' USING PigStorage('|') AS (movieId:chararray,title:chararray);

-- LOAD usuarios
users = LOAD 'pr03_2/u.user'  USING PigStorage('|') AS (userId:chararray,age:int,gender:chararray,rol:chararray);

-- JOIN unimos las 3 tablas en una nueva tabla
data = JOIN votes BY userId, users BY userId;
data = JOIN data BY votes::movieId, movies BY movieId;

--  FOREACH generamos un nuevo bag con los campos que necesitamos
dataNew = FOREACH data GENERATE movies::movieId AS movieId,movies::title AS titulo, users::rol AS rol, votes::rating AS rating;

-- GRPOUP nuevo grupo por rol y tiulo
dataGroup = GROUP dataNew BY (rol, titulo);

-- FOREACH calculamos la media por cada grupo y lo extraemos en diferenets lineas con flatten
mediaRating = FOREACH dataGroup GENERATE FLATTEN(group) AS (rol, titulo),AVG(dataNew.rating) AS media;

-- GROUP agrupamos por rol
grupoFinal = GROUP mediaRating BY rol;

-- FOREACH cada grupo lo ordenamos por media, y seleccionamos la primera posicion
bestMovieRol = FOREACH grupoFinal {ordenar= ORDER mediaRating BY media DESC; bestMovie= LIMIT ordenar 1; GENERATE FLATTEN(bestMovie);};

-- STORE almacenmos salida
STORE bestMovieRol INTO 'movies_analisis/bestMovieRol' USING PigStorage(',');






