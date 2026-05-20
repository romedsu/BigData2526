--LOAD u.data
votes= LOAD 'pr03_2/u.data' USING PigStorage('\t') AS (userId:chararray,movieId:chararray,rating:int);

--LOAD u.item
movies = LOAD 'pr03_2/u.item' USING PigStorage('|') AS (movieId:chararray,title:chararray);

-- COGROUP (agrupamos las dos tablas por id de la película)
moviesGrupo = COGROUP movies BY movieId, votes BY movieId;

-- FOREACH votacion total (sumar total puntuaciones)
totalVotes = FOREACH moviesGrupo GENERATE group,movies.title,SUM(votes.rating) AS puntuacion;

-- ORDENAR de mayor a menor puntuación
ordenar = ORDER totalVotes BY puntuacion DESC; 

--LIMIT (seleccionar 5 mas votadas)
top5movies = LIMIT ordenar 5;  

--STORE (alamcenar el resultado)
STORE top5movies INTO 'movies_analisis/top5movies' USING PigStorage(',');

-- MOSTRAR por pantalla
dump top5movies;







