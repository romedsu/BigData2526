-- CARGA DATOS
ventas = LOAD 'pr03_1/retail_sales_dataset.csv' USING PigStorage(',') AS (ventaID:int, fecha:chararray, clienteID:chararray, genero:chararray, edad:int, categoria:chararray, cantidad:int, precioUnidad:double, precioTotal:double);


-- AÑADIR IVA (IVA y total conIVA)
ventasUpdate = FOREACH ventas GENERATE ventaID, fecha, clienteID, genero, edad, categoria, cantidad, precioUnidad, precioTotal,precioTotal * 0.21 AS IVA, precioTotal * 1.21 AS totalIVA;


-- FILTER (por categoría Beauty y clientes mayores 30)
clientes30BeautyFiltro= FILTER ventasUpdate BY categoria == 'Beauty' AND edad >30;


-- ORDER
orderClientes30Beauty = ORDER clientes30BeautyFiltro BY totalIVA DESC;


-- LIMIT
topClientes30Beauty = LIMIT orderClientes30Beauty 10;


-- GROUP
clientes30BeautyGrupo= GROUP clientes30BeautyFiltro ALL;


-- CANTIDAD total y GASTO MEDIO
totalClientes30BeautyMedia = FOREACH clientes30BeautyGrupo GENERATE group, COUNT(clientes30BeautyFiltro) AS cantidadClientes, AVG(clientes30BeautyFiltro.totalIVA) AS gastoMedio;


-- STORE
STORE topClientes30Beauty INTO 'venta_analisis/topClientes30Beauty' USING PigStorage(',');

STORE totalClientes30BeautyMedia INTO 'venta_analisis/totalClientes30BeautyMedia' USING PigStorage(',');