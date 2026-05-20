--LOAD u.data
votes= LOAD 'pr03_2/u.data' USING PigStorage('\t') AS (userId:chararray,movieId:chararray,rating:double);

--LOAD u.item
movies = LOAD 'pr03_2/u.item' USING PigStorage('|') AS (movieId:chararray,title:chararray,releaseDate:chararray);

-- COVENTIR fecha a tipo de dato :date )(ToDate())
moviesUpdate = FOREACH movies GENERATE movieId,title,ToDate(releaseDate,'dd-MMM-yyyy') AS releaseDate;

-- COGROUP (agrupamos las dos tablas por id de la película)
moviesGrupo = COGROUP moviesUpdate BY movieId, votes BY movieId;

-- FOREACH  (media puntuaciones)
-- Uso de FLATTEN para desempaquetar el titulo y poder mostrarlo más estéticamente
mediaVotes = FOREACH moviesGrupo GENERATE group,FLATTEN (moviesUpdate.title) AS titulo ,FLATTEN(moviesUpdate.releaseDate) AS fecha, ROUND(AVG(votes.rating)*100)/100.0 AS media;

-- FILTER
moviesFilter = FILTER mediaVotes BY media >4.0;

-- ORDENAR por fechas (más antiguas)
ordenar = ORDER moviesFilter BY fecha; 

--LIMIT (seleccionar 5 películas mas antiguas)
top5moviesOld = LIMIT ordenar 5;  

--STORE (alamcenar el resultado)
STORE top5moviesOld INTO 'movies_analisis/top5moviesOld' USING PigStorage(',');
