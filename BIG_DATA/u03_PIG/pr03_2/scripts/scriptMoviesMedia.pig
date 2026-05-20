--LOAD u.data
votes= LOAD 'pr03_2/u.data' USING PigStorage('\t') AS (userId:chararray,movieId:chararray,rating:int);

--LOAD u.item
movies = LOAD 'pr03_2/u.item' USING PigStorage('|') AS (movieId:chararray,title:chararray);

-- COGROUP (agrupamos las dos tablas por id de la película)
moviesGrupo = COGROUP movies BY movieId, votes BY movieId;

-- FOREACH  (media puntuaciones)
-- Uso de FLATTEN para desampaquetar el titulo y poder mostrarlo más estéticamente
mediaVotes = FOREACH moviesGrupo GENERATE group,FLATTEN (movies.title) AS titulo ,AVG(votes.rating) AS media;

-- ORDENAR de mayor a menor media
ordenar = ORDER mediaVotes BY media DESC; 

--LIMIT (seleccionar 10 películas con mas media)
top10moviesMedia = LIMIT ordenar 10;  

--STORE (alamcenar el resultado)
STORE top10moviesMedia INTO 'movies_analisis/top10moviesMedia' USING PigStorage(',');
