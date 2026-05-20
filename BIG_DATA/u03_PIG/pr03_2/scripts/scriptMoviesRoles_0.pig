-- LOAD votaciones
votes = LOAD 'pr03_2/u.data' USING PigStorage('\t') AS (userId:chararray,movieId:chararray,rating:double);

-- LOAD movies
movies = LOAD 'pr03_2/u.item' USING PigStorage('|') AS (movieId:chararray,title:chararray);

-- LOAD usuarios
users = LOAD 'pr03_2/u.user'  USING PigStorage('|') AS (userId:chararray,age:int,gender:chararray,rol:chararray);

-- COGROUP (agrupamos las dos tablas por id de la película)
--moviesGrupo = COGROUP movies BY movieId, votes BY movieId;

-- JOIN
userJoin = JOIN users BY userId, votes BY userId;


-- GROUP por roles
rolGrupo = GROUP userJoin BY (users::rol,votes::movieId);



mediaGrupo = FOREACH rolGrupo GENERATE group,AVG(userJoin.votes::rating) AS media;

mediaGrupoTitulo = JOIN mediaGrupo BY movieId,movies BY movieId;






