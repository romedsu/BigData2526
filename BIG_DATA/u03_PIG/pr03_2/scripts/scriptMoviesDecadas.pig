-- LOAD votaciones
votes = LOAD 'pr03_2/u.data' USING PigStorage('\t') AS (userId:chararray,movieId:chararray,rating:double);

-- LOAD movies
movies = LOAD 'pr03_2/u.item' USING PigStorage('|') AS (movieId:chararray,title:chararray);

-- FOREACH extraer el año del título usando regex_extract (substring no permite numero negativos)
moviesYear = FOREACH movies GENERATE movieId, (int)REGEX_EXTRACT(title, '.*\\((\\d{4})\\)', 1) AS releaseYear;

-- FOREACH calcular decada de cada año (/10*10) para obtener del año, la década
moviesDecade = FOREACH moviesYear GENERATE movieId,(int)(releaseYear / 10) * 10 AS decade;

-- JOIN unir las películas con su década y las votaciones
data = JOIN votes BY movieId, moviesDecade BY movieId;

-- GROUP agrupar por la década
groupDecade = GROUP data BY moviesDecade::decade;

-- FOREACH media de las votaciones por década (redondeo *100/100 para obtener sólo 2 decimales)
mediaRating = FOREACH groupDecade GENERATE group AS decade, (double)ROUND(AVG(data.votes::rating)*100)/100 AS media;

-- ORDER ordenar por década 
ratingDecade = ORDER mediaRating BY decade ASC;

-- STORE alamcenar
STORE ratingDecade INTO 'movies_analisis/ratingDecade' USING PigStorage(',');