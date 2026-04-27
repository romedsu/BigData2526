# %% EJERCICIO 1
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 11:05:43 2026

@author: Mañana
"""

'''
1 Crear una funcion que construya un DataFrame a partir del fichero 
cotizacion.csv.
Se deberá realizar usando el formato de creación de DataFrames de clave-valor,
 de la forma:
pd.DataFrame({'col1':serie1, 'col2':serie2}) siendo col1 las columnas y serie
 los datos de cada columna
 a) Crear la funcion cotizaciones
b) leer el fichero indicando separador (;) , los miles (.) y decimal (,)
c) Eliminar la columna 'Nombre'
d) Crear DataFrame usando clave:valor y asignarle columnas 'Minimo','Maximo','Media'
e) Retornar el dataframe creado e imprimirlo desde fuera de la función
'''
import pandas as pd

#ruta=r'C:\Users\Mañana\OneDrive - Consejería de Educación\Documentos\rm\SAA_MIA\u03_apredizaje_supervisado\ejercicios\cotizacion.csv'

ruta='datasets/cotizacion.csv'

def cotizaciones(ruta):
    datos=pd.read_csv(ruta,sep=';',thousands='.',decimal=',')

    datos=datos.drop(columns=['Nombre'])

    dfDatos=pd.DataFrame({
        'Minimo':datos.min(),
        'Maximo':datos.max(),
        'Media':datos.mean()
        })

    # print(dfDatos.head())

    return(dfDatos)
   
    
print(cotizaciones(ruta))
   


#%% TITANIC (1ªparte)

'''
2 Analiza el archivo csv y busca en la documentación cómo usar los distintos métodos:
a) Genera un dataframe con los datos de titanic.csv
b) Imprima dimensiones, tamaño, indice y las 10 ultimas lineas del dataframe
c) Datos del pasajero con identificador 148 con loc[] (ojo indexacion desde cero)
d) Mostrar por pantalla las filas pares usando iloc[range(...)]
e) Nombres de personas de primera clase 'Pclass==1' ordenadas alfabeticamente
'''
# import pandas as pd

rutaTitanic='datasets/titanic.csv'

datosTitanic=pd.read_csv(rutaTitanic,sep=',')

dfTitanic=pd.DataFrame(
    datosTitanic,
    index=datosTitanic.index,
    columns=datosTitanic.columns)

print(f"DIMENSIONES:\n {dfTitanic.shape}")
print(f'TAMAÑO:\n {dfTitanic.size}')
print(f'INDEX:\n {dfTitanic.index}')
print(f'ULTIMOS 10: {dfTitanic.tail(10)}')

print(f'PASAJERO 148:\n {dfTitanic.loc[147]}')

#PASAJEROS PARES
pasajerosPares=dfTitanic.iloc[range(0,len(dfTitanic),2)]
print(f'PASAJEROS PARES:\n {pasajerosPares}')

# print(f'PASAJEROS PARES {dfTitanic.iloc[range(0,len(dfTitanic),2)]}')

#PRIMERA CLASE
primeraClase=dfTitanic.loc[dfTitanic['Pclass']==1]

#ORDENAR por nombre
primeraClase=primeraClase.sort_values('Name',ascending=True)

#Sumamos 1 al index, para que coincidan el index y el id del pasajero
primeraClase.index=primeraClase.index+1
print(f'PASAJEROS 1ªCLASE:\n {primeraClase}')

# primeraClase=dfTitanic.loc[dfTitanic['Pclass']==1,'Name'].sort_values()
# primeraClase.index=primeraClase.index+1


#%% TITANIC (2ªparte)

'''
3 Continuando con el archivo csv de titanic, investiga cómo usar los métodos:
a) Imprimir porcentaje de supervivientes con .value_counts(normalize=True)*100
b) Porcentaje de supervivientes de cada clase, usando .groupby('Pclass')['Survived']
c) Eliminar los pasajeros con edad desconocida con dropna()
d) Edad media (mean) de las mujeres que viajaban de cada clase, ['Sex']=='female'....
e) Añadir columna booleana 'Young' para ver si pasajero era menor de edad
f) Mostrar todas las columnas del dataframe usando pd.set_option(...)
'''
#PORCENTAJE SUPERVIVIENTES
supervivientes=dfTitanic['Survived'].value_counts(normalize=True)*100

print(f'\nSUPERVIVIENTES:\n {supervivientes}\n\n')


#PORCENTAJE de cada CLASE (con GROUP BY)
supervivientesClase=dfTitanic.groupby('Pclass')['Survived'].value_counts(normalize=True)*100
print(f'\nSUPERVIVIENTES x CLASE:\n {supervivientesClase}\n\n')

#ELIMINAR NaN de columna (con una copia)
dfTitanicUp=dfTitanic.dropna(subset=['Age']).copy()
print(dfTitanicUp)


#MEDIA de MUJERES por CLASE
media= dfTitanicUp[dfTitanicUp['Sex']=='female'].groupby('Pclass')['Age'].mean()

print(f"\nMEDIA: {media}")


#AÑADIR COLUMNA (booleana)
dfTitanicUp['Young']=dfTitanicUp['Age']<18

print(f"\nMENORES:\n {dfTitanicUp['Young']}\n\n")


# TODAS LAS COLUMNAS DE DF
# configuracion de como mostrar por terminal (todas las filas -> max_rows)
pd.set_option('display.max_columns', None)

print(dfTitanicUp)

#%% EJER 4

'''
4 Los ficheros emisiones-201X.csv contienen datos sobre las emisiones contaminantes 
('MAGNITUD') en la ciudad de Madrid.
a) Generar el DataFrame 'emisiones' con los datos de los 4 ficheros conjuntos usando .concat
    
b) Filtrar las columnas para quedarse con Estacion, Magnitud, Año y Mes de los dias D01, D02, etc
    
c) Reestructurar el DataFrame para que los valores de los contaminantes de las
    columnas de los dias aparezcan en una única columna usando .melt(id_vars=[...]))
    
d) (import datetime) Crear columna FECHA con la concatenación del año, mes, día.
    (usar método emisiones.DIA.str.strip() y emisiones.ANO.astype(str)))
    
e) Eliminar filas con fechas no validas usando numpy.isnat(...)
'''

import pandas as pd

# A) GENERAR DATAFRAME con todos los datasets
data2016=pd.read_csv('datasets/emisiones2016.csv', sep=';')
data2017=pd.read_csv('datasets/emisiones2017.csv', sep=';')
data2018=pd.read_csv('datasets/emisiones2018.csv', sep=';')
data2019=pd.read_csv('datasets/emisiones2019.csv', sep=';')


'''
df2016=pd.DataFrame(data2016,
                    index=data2016.index,
                    columns=data2016.columns)

df2017=pd.DataFrame(data2017,
                    index=data2017.index,
                    columns=data2017.columns)

df2018=pd.DataFrame(data2018,
                    index=data2018.index,
                    columns=data2018.columns)

df2019=pd.DataFrame(data2019,
                    index=data2019.index,
                    columns=data2019.columns)
'''
df2016=pd.DataFrame(data2016)

df2017=pd.DataFrame(data2017)

df2018=pd.DataFrame(data2018)

df2019=pd.DataFrame(data2019)


emisiones=pd.concat([df2016,df2017,df2018,df2019])

print(f'\nEMISIONES DFs:\n {emisiones.head()}\n')


# B) FILTRAR columna ESTACION,MAGNITUD, AÑO, MES y DIAS (D01,D02..)
columnas=['ESTACION','MAGNITUD','ANO','MES']
print(f'\nCOLUMNAS:\n {columnas}\n')

# añadir todas las columnas que empiezan por D (dias)
columnas.extend([col for col in emisiones.columns if col.startswith('D')])

emisiones=emisiones[columnas]

print(f'\nEMISIONES filtradas:\n {emisiones.head()}\n')


# C) REESTTRUCTURAR DF, varias columnas en una nueva ( .melt() ) (fundir))
# id_vars --> columnas originales
# var_name --> nombre nueva columna que agrupa las columnas (Si no se especifica, usa todas las que no están en id_vars)
# value_name --> nombre de la nueva columna que contendrá los datos
emisionesReest= emisiones.melt(
    id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'],
    var_name='DIA',
    value_name='VALOR')

print(f'\nEMISIONES reestructuradas:\n {emisionesReest.head()}\n')


# D) NUEVA COLUMNA fecha (concatenando ano,mes y dia)
# import datetime
import numpy as np

# eliminar la D de los valores de DIA (D01, etc)
emisionesReest['DIA']=emisionesReest['DIA'].str.strip('D')

# astype(str) --> convertir datos numéricos en str y concatenamos
fecha= (emisionesReest['DIA'].astype(str) + '-'+
        emisionesReest['MES'].astype(str)+'-'+
        emisionesReest['ANO'].astype(str)
        )
        

#convertir str anterior en tipo date y darle formato fecha( uso de %) y errors
# errors='coerce' --> en vez de NaN, not a time
emisionesReest['FECHA']=pd.to_datetime(fecha,format='%d-%m-%Y', errors='coerce')


# BORRAR FILAS CON FECHA NAN
# ~ (Operador NOT): Invierte el resultado booleano. 
# En lugar de seleccionar los valores nulos, selecciona los valores que no son nulos (las fechas válidas)
emisionesReest=emisionesReest[~np.isnat(emisionesReest['FECHA'])]

# emisionesReest=emisionesReest[np.isnat(emisionesReest['FECHA']=='False')]

print(f"\nFECHA: \n{emisionesReest['FECHA']}")

print(f"\nFINAL: \n{emisionesReest.head()}")

# ordenar por mes y dia
# print(f"\nFINAL: \n{emisionesRest.sort_values(by=['MES','DIA']).head()}")

# borrar columnas de año,mes y dia (quedaria fecha)
# emisionesRest=emisionesRest.drop(columns=['ANO','MES','DIA'])

print(f"\nFINAL: \n{emisionesReest.head()}")

# pd.set_option('display.width', 1000)

# Muestra las primeras 5 filas perfectamente alineadas
# print(f'FINAL TAB: \n{emisionesRest.head().to_string(index=False)}')

# %% Ej 5 emisiones continuacion

'''
5 Continuar con el ejercicio anterior para los siguientes apartados:
    
f) ordenar las columnas en este orden Estacion, Magnitud, Fecha
    
g) Función que reciba una estación, un contaminante y un rango de fechas y 
    devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
    
h) Mostrar un resumen descriptivo (min, MAX, media) para cada contaminante usando .groupby(...).VALOR.describe()
    
i) Mostrar resumen descriptivo para cada contaminante por distritos (estaciones) ampliando el código del apartado anterior
    
j) Función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada.
    
k) Función que devuelva emisiones medias mensuales de un contaminante y un año dados para todas las estaciones
    
l) Función que reciba estación y devuelva DataFrame con medias mensuales de los tipos de contaminantes
'''

# f) ORDENAR  las columnas en este orden Estacion, Magnitud, Fecha
# emisionesReest= emisionesReest.sort_values(by=['ESTACION','MAGNITUD','FECHA'],ascending=True)

# corregido
# ORDENAR LAS COLUMNAS (no los valores) en ese orden
columnas1=['ESTACION','MAGNITUD','FECHA']
columnas2=[col for col in emisionesReest.columns if col not in columnas1]

columnasFinal=columnas1+columnas2

emisionesReest=emisionesReest[columnasFinal]

print(emisionesReest.head())


# G)FUNCION

# def emisionFn(estacion,magnitud,fechaInicio,fechaFin):
#     filtro = ((emisionesReest['ESTACION'] == estacion) & 
#        (emisionesReest['MAGNITUD'] == magnitud) & 
#        (emisionesReest['FECHA'].between(pd.to_datetime(fechaInicio), pd.to_datetime(fechaFin))))


# corregido
def emisionFn(estacion,magnitud,fechaInicio,fechaFin):
    filtro = ((emisionesReest['ESTACION'] == estacion) & 
       (emisionesReest['MAGNITUD'] == magnitud) & 
       (emisionesReest['FECHA']>= fechaInicio) & (emisionesReest['FECHA']<= fechaFin))
    
    return emisionesReest.loc[filtro,'VALOR'].copy()
    
 
valor=emisionFn(4,1,'2016-01-01','2016-02-01')

print(f'RESULTADO funcion emisionFn: \n{valor}\n')

#%% H) RESUMEN DESCRIPTIVO (min,max,media) para cada contaminante usando .groupby(...).VALOR.describe()

# funciona tb .groupby(['MAGNITUD'])
# Solo mostrar estas operaciones --> [['min','max','mean']]

# tb valida
# resumenDescribe= emisionesReest.groupby(emisionesReest['MAGNITUD'])['VALOR'].describe()[['min','max','mean']]

resumenDescribe= emisionesReest.groupby(emisionesReest['MAGNITUD']).VALOR.describe()[['min','max','mean']]

print(f'RESUMEN DESCRIBE:\n {resumenDescribe}\n')



#%% I) Mostrar resumen descriptivo para cada contaminante por distritos (estaciones) ampliando el código del apartado anterior

resumenDescibeDistritos= emisionesReest.groupby(['MAGNITUD','ESTACION']).VALOR.describe()[['min','max','mean']]
print(f'RESUMEN DESCRIBE DISTRITOS:\n {resumenDescibeDistritos}\n')


# %% J) Función que reciba una estación y un contaminante y devuelva 
# un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada

def emision2Fn (estacion,magnitud):
    filtro = (emisionesReest['ESTACION'] == estacion) & (emisionesReest['MAGNITUD'] == magnitud)
    
    resultado= emisionesReest.loc[filtro].VALOR.describe()
    return resultado

valor2= emision2Fn(4,1)

print(valor2)

# %% k) Función que devuelva emisiones medias mensuales de un contaminante y un año dados para todas las estaciones
def emisiones3Fn (magnitud, anio):
    filtro = (emisionesReest['MAGNITUD'] == magnitud) & (emisionesReest['ANO'] == anio)
    print(filtro)
    
    resultado = emisionesReest.loc[filtro].groupby(['ESTACION', 'MES']).VALOR.mean()
    
    return resultado

mediaMensual = emisiones3Fn(1, 2016)

print(f'MEDIA MENSUAL POR ESTACION Y MES:\n {mediaMensual}\n')

# %% l) Función que reciba estación y devuelva DataFrame con medias mensuales de los tipos de contaminantes

def emisiones4Fn(estacion):
    filtro = (emisionesReest['ESTACION'] == estacion)
    
    resultado = emisionesReest.loc[filtro].groupby(['MAGNITUD', 'MES']).VALOR.mean()
    
    return resultado

mediasMensualesEstacion = emisiones4Fn(4)

print(f'MEDIAS MENSUALES POR CONTAMINANTE Y MES (ESTACION 4):\n {mediasMensualesEstacion}\n')



# %% EJERCICIOS 26

'''
Desarrolla un modelo de regresión lineal múltiple para predecir el precio de las
 casas en California de acuerdo con el número de habitaciones que tiene la vivienda,
 el tiempo que ha estado ocupada y la distancia a los centros de trabajo de California.
 Estas son varias características que se tomarán en cuenta para diseñar nuestro modelo. 
 Para ello, utiliza el conjunto de datos fetch_california_housing() de los datasets de scikit-learn.

En este ejercicio vas a construir un modelo de regresión lineal para predecir
 el precio medio de viviendas en California utilizando el dataset California Housing
 disponible en sklearn. Sigue los siguientes pasos:

a)	 Importa las librerías necesarias:
•	pandas
•	fetch_california_housing desde sklearn.datasets
•	train_test_split desde sklearn.model_selection
•	LinearRegression desde sklearn.linear_model
•	mean_squared_error y r2_score desde sklearn.metrics
•	StandardScaler desde sklearn.preprocessing

b)	Carga el dataset California Housing.
 
c)	Crea un DataFrame de pandas con las variables predictoras y añade 
    una nueva columna llamada PRICE que contenga la variable objetivo 
    (usando el atributo .target de los datos cargados)
 
d)	Selecciona como variables independientes las siguientes características:
    MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude.
 
e)	Separa el conjunto de datos en Variables predictoras (X) con las 
    caracteristicas del dataframe y Variable objetivo (y) con la columna de PRICE
 
f)	Divide los datos en conjunto de entrenamiento y prueba: 80% entrenamiento,
    20% prueba y usa random_state=42
    
'''

# a)
from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
# from sklearn.preprocessing import StandardScaler


# b)
# datosHousing = datasets.fetch_california_housing(as_frame=True)
datosHousing= datasets.fetch_california_housing()

print("\n ------DATASET------")
print(datosHousing)

print("\n ------Nombres de las caracteristicas COLUMNAS------")
print(datosHousing.feature_names)


print("\n ------Nombres del objetivos------")
print(datosHousing.target_names)

print("\n ------Nombres del frame------")
print(datosHousing.frame)

# print("\n ------Nombres del filename------")
# print(datosHousing.filename)

print("\n ------Descripción------")
print(datosHousing.DESCR)


# c)DATAFRAME

# hay que poner .data
# OPCION ALTERNATIVA --> dfHousing = datosHousing.frame (hay que poner (as_frame=True) )
# dfHousing = datosHousing.frame
dfHousing = pd.DataFrame(datosHousing.data,
                         columns=datosHousing.feature_names)

print("\n ------DATAFRAME HOUSING------")
print(dfHousing.head())


print("\n ------DATAFRAME HOUSING - PRICE (Columna añadida) OBJETIVO------")
# OBJETIVO
dfHousing['PRICE']=datosHousing.target
print(dfHousing.head())


#%% D VARIABLES INDEPENDIENTES

X = dfHousing[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']]

# Y = dfHousing['PRICE']

print("\n ------VARIABLES INDEPENDIENTES (X)------")
print(X.head())


# %% E

# Variables predictoras (X): todas las características menos el precio
# X = dfHousing.drop('PRICE', axis=1)

# Variable objetivo (y): solo la columna del precio
Y = dfHousing['PRICE']

# Verificación de la separación
print(f"Dimensiones de X: {X.shape}") # Debería mostrar (20640, 8)
print(f"Dimensiones de y: {Y.shape}") # Debería mostrar (20640,)


# %% F

# División de los datos
# test_size=0.2 indica el 20% para prueba y, por defecto, el 80% para entrenamiento.
# random_state --> semilla (puede ser cualquier número)

X_train, X_test, Y_train, Y_test = train_test_split(X,
                                                    Y,
                                                    test_size=0.2, 
                                                    random_state=42)

# Verificación de los tamaños
print(f"Registros para entrenamiento: {len(X_train)}")
print(f"Registros para prueba: {len(X_test)}")

# %%
'''
g)	Aplica una normalización (escalado) de los datos utilizando StandardScaler:
    Ajusta el escalador con los datos de entrenamiento. Transforma tanto los datos
    de entrenamiento como los de prueba.

h)	Crea la variable modelo, instancia de LinearRegression() y usa su método fit()
    pasándole como parametros el X_train escalado y el y_train.

i)	Crea la variable ‘prediccionConjuntoPrueba’ y realiza predicciones sobre 
    el conjunto de prueba con el método .predict() usando de parametro el X_test escalado

j)	Calcula Error Cuadrático Medio (MSE) en una variable usando mean_squared_error(),
    con parametros y_test y la prediccion del conjunto de prueba. Muéstralo por pantalla

k)	 Calcula el Coeficiente de Determinación (R²) en una variable usando r2_score(),
    con parametros y_test y la prediccion del conjunto de prueba. Muéstralo por pantalla.
l)	Muestra por pantalla todos los valores (MedInc, HouseAge, AveRooms,etc) a los que
    se pueden acceder mediante el método modelo.coef_

'''

# G --<StandardScaler>--

print("\n -----STANDARDSCALER ----")
from sklearn.preprocessing import StandardScaler

scaler= StandardScaler()

# SOLO 1 DATO POR FIT_TRANSFORM
X_train_scaler =scaler.fit_transform(X_train)

# sin fit el de X_TEST (solo transform)
X_test_scaler =scaler.transform(X_test)

print(X_train_scaler)

print(X_test_scaler)



# %% H - LINEAR REGRESSION
from sklearn import linear_model 

modelo =linear_model.LinearRegression()


modelo.fit(X_train_scaler,Y_train) 


w = modelo.coef_ 
b = modelo.intercept_ 
print(f"\nPESOS - Primer coeficiente (w1): {w[0]}") 
print(f"SESGO - Intercepto (b): {b}")



#%% I 

prediccionTest = modelo.predict(X_test_scaler)

# %% J - ERROR CUADRÁTICO MEDIO
mse = mean_squared_error(Y_test,prediccionTest)


print(f'\n MSE \n{mse}')


# %% K - COEFICIENTE DE DETERMINACIÓN (R²)

coef_determinacion =r2_score(Y_test,prediccionTest)

print(f'\n coeficiente_determinacion \n{coef_determinacion}')



# %%L
for dato in modelo.coef_:
    print(dato)


# %% EJERCICIO 27

'''
27 Desarrolla un modelo de clasificación mediante Regresión Logística para predecir 
la especie de flor Iris utilizando únicamente el largo y el ancho del sépalo.
En este ejercicio vas a construir un modelo de clasificación supervisada usando
 el dataset load_iris() de scikit-learn. El objetivo es entrenar 
 un modelo de Regresión Logística, evaluarlo con métricas de clasificación y
 visualizar su frontera de decisión.
 
a) Importa las siguientes librerías:
• numpy como np
• pandas como pd
• load_iris desde sklearn.datasets
• train_test_split desde sklearn.model_selection
• LogisticRegression desde sklearn.linear_model
• StandardScaler desde sklearn.preprocessing
• accuracy_score, classification_report y confusion_matrix desde sklearn.metrics
• matplotlib.pyplot como plt
 
b) Carga el dataset Iris en una variable llamada datosIris utilizando:
datosIris = load_iris()
 
c) Crea un DataFrame llamado dfIris con:
• Las variables predictoras usando datosIris.data
• Los nombres de columnas usando datosIris.feature_names
Añade una nueva columna llamada target usando: dfIris['target'] = datosIris.target
 
d) Crea un array llamado caracteristicas con las siguientes 
    variables independientes:  'sepal length (cm)' y  'sepal width (cm)'
 
e) Separa el conjunto de datos en: variable X con dfIris[caracteristicas] y 
    variable y con dfIris['target']
 
f) Divide los datos en conjunto de entrenamiento y prueba utilizando:
    train_test_split(X, y, test_size=0.2, random_state=42)
    
'''
# A)
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

import matplotlib.pyplot as plt

# B)
datosIris=datasets.load_iris()

print(f'\n datosIris feature_names \n {datosIris.feature_names}')

print(f'\n datosIris target_names \n {datosIris.target_names}')

print(f'\n datosIris KEYS \n {datosIris.keys()}')


# C) CREAR DATASET
dfIris= pd.DataFrame(datosIris.data,
                     columns=datosIris.feature_names)

print(f'\n dfIris \n {dfIris.head()}')




# OBJETIVO nueva columna
dfIris['target']=datosIris.target

print(f'\n OBJETIVO: dfIris["target"] \n {dfIris["target"]}')



# D) variables independientes (array)
caracteristicas = ['sepal length (cm)','sepal width (cm)']

print(f'\n CARACTERISTICAS \n{caracteristicas}')

print(f'\n dfIris[caracteristicas] \n {dfIris[caracteristicas]}')


# E) VARIABLES X e Y (caracteriticas y objetivo)
X= dfIris[caracteristicas]

Y =dfIris['target']

print(f'\n X \n{X}')
print(f'\n Y \n{Y}')



# F) TRAIN TEST SPLIT
X_train,X_test,Y_train,Y_test= train_test_split(X,
                                                Y,
                                                test_size=0.2,
                                                random_state=42)



# %% 27 B

'''
g) Aplica una normalización utilizando StandardScaler:
    • Crea una instancia llamada scaler
    
    • Ajusta y transforma los datos de entrenamiento con: 
        escalaAjusteEntrenamiento = scaler.fit_transform(X_train)
        
    • Transforma los datos de prueba con: escalaAjustePrueba = scaler.transform(X_test)
 
h) Crea la variable ‘modelo’ como una instancia de LogisticRegression() 
    y entrena modelo usando modelo.fit(escalaAjusteEntrenamiento, y_train)
 
i) Realiza las predicciones sobre el conjunto de prueba utilizando:
    predicionesPrueba = modelo.predict(escalaAjustePrueba)
 
j) Evalúa la precisión del modelo calculando la variable accuracy usando:
    accuracy_score(y_test, predicionesPrueba) y mostrándola por pantalla.
 
k) Genera y muestra el informe de clasificación usando: 
    classification_report(y_test, predicionesPrueba) y la matriz de confusión
    almacenándola en una variable llamada matrizConfusion usando: 
        confusion_matrix(y_test, predicionesPrueba)
 
l) Visualización de la frontera de decisión (solo si el número de características es 2):
    • Crea una malla de puntos usando este código:
        x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
        y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
        
    • Predice las clases sobre la malla con este código
        Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
 
m)  Usa plt.contourf() para dibujar la superficie, plt.scatter() para representar
    los puntos de entrenamiento y añade etiquetas a los ejes
    y un título con plt.xlabel() y plt.title()
    
'''


# G) STANDARSCALER (normalizacion) (aprende media y desviacion tipica y despues lo transforma)

scaler= StandardScaler()

escalaAjusteEntrenamiento= scaler.fit_transform(X_train)

escalaAjustePrueba= scaler.transform(X_test)



# H) MODELO (crear y entrenar)

# modelo= linear_model.LogisticRegression()

modelo= LogisticRegression()

modelo.fit(escalaAjusteEntrenamiento,Y_train)



#I) PREDICCIONES

predicionesPrueba= modelo.predict(escalaAjustePrueba)

print(f'\n predicionesPrueba: \n {predicionesPrueba}')


    
# J) PRECISION modelo (ACCURACY)

precision=accuracy_score(Y_test, predicionesPrueba)

print(f'\n PRECISION accuracy_score: \n {precision}')




# K) INFORME CLASIFICACION

informe= classification_report(Y_test, predicionesPrueba)
print(f'\n INFORME CLASIFICACION: \n {informe}')




# K b) NATRIZ CONFUSION

matrizConfusion= confusion_matrix(Y_test, predicionesPrueba)

print(f'\n MATRIZ CONFUSION: \n {matrizConfusion}')


# L) FRONTERA de DECISION (sobre el escalado (standarScaler) del X_train)
x_min, x_max = escalaAjusteEntrenamiento[:, 0].min() - 1, escalaAjusteEntrenamiento[:, 0].max() + 1


y_min, y_max = escalaAjusteEntrenamiento[:, 1].min() - 1, escalaAjusteEntrenamiento[:, 1].max() + 1

xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))


# PREDICCION de CLASES sobre malla
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

print(f'\n Z: \n {Z}')



# M) PLT (graficos)

# gráficos de contorno rellenos
plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')


# gráficos de dispersión 

# [:, 0] --> fila 0 (1º)
# [:, 0] --> fila 1 (2º)
plt.scatter(escalaAjusteEntrenamiento[:, 0], 
            escalaAjusteEntrenamiento[:, 1], 
            c=Y_train, 
            edgecolors='k', 
            cmap='viridis')


plt.xlabel('Sepal length (estandarizado)')
plt.ylabel('Sepal width (estandarizado)')
plt.title('Fronteras de Decisión: Regresión Logística (Iris)')

plt.show()



# %% EJERCICIO 28

'''
28  Evalúa un modelo de Regresión Logística mediante validación cruzada para
     clasificar las especies Iris utilizando el largo y el ancho del sépalo.
     En este ejercicio vas a construir un modelo de clasificación supervisada 
     utilizando el dataset load_iris() de scikit-learn. A diferencia del ejercicio 
     anterior, no realizarás una única división en entrenamiento y prueba,
     sino que evaluarás el modelo mediante validación cruzada con 5 pliegues 
     para obtener una estimación más robusta de su rendimiento. Posteriormente,
     entrenarás el modelo con todos los datos para visualizar la frontera de decisión.
     
     
    a) Importa las siguientes librerías:
        • numpy como np
        • pandas como pd
        • matplotlib.pyplot como plt
        • load_iris desde sklearn.datasets
        • cross_val_score desde sklearn.model_selection
        • LogisticRegression desde sklearn.linear_model
        • StandardScaler desde sklearn.preprocessing
        
    b) Carga el dataset Iris en una variable llamada datosIris utilizando datosIris = load_iris()
    
    
    c) Crea un DataFrame llamado dfIris con las variables predictoras 
        usando datosIris.data y los nombres de columnas usando datosIris.feature_names. 
        Después añade una nueva columna llamada target usando dfIris['target'] = datosIris.target
        
        
    d) Crea un array llamado caracteristicas con las siguientes variables independientes:
        'sepal length (cm)' y 'sepal width (cm)'
        
        
    e) Separa el conjunto de datos en variable X con dfIris[caracteristicas] y
        variable y con dfIris['target']
        
        
    f) Aplica una normalización utilizando StandardScaler. Crea una instancia
        llamada scaler, ajusta y transforma todos los datos utilizando:
            X_scaled = scaler.fit_transform(X)
            
            
    g) Crea la variable modelo como una instancia de LogisticRegression().

'''

# A)
    
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

# from sklearn.datasets import load_iris

from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import StandardScaler


#  B)

datosIris = load_iris()


# C)
dfIris= pd.DataFrame(datosIris.data,
                     columns=datosIris.feature_names)

    # nueva columna OBJETIVO
dfIris['target']=datosIris.target



# D) CARACTERISTICAS

caracteristicas = ['sepal length (cm)','sepal width (cm)']


# E)
X = dfIris[caracteristicas]

Y =dfIris['target']


# F)STANDAR SCALER
# media de 0 y una desviación estándar de 1

scaler= StandardScaler()

    # SOLO 1 DATO POR FIT_TRANSFORM
X_scaled =scaler.fit_transform(X)




# G) MODELO  --> LogisticRegression()

modelo= LogisticRegression()

modelo.fit(X_scaled,Y)


'''
h) Realiza una validación cruzada con 5 pliegues utilizando 
    cv_accuracy = cross_val_score(modelo, X_scaled, y, cv=5, scoring='accuracy')
    Muestra por pantalla: El vector de precisiones obtenido en cada pliegue y
    la precisión media calculada mediante np.mean(cv_accuracy)
    
    
i) Entrena el modelo con todos los datos escalados utilizando modelo.fit(X_scaled, y)
    
    
j) Visualización de la frontera de decisión:
    • Calcula los valores mínimos y máximos de cada característica usando X_scaled[:, 0] y X_scaled[:, 1]
    
    • Crea una malla de puntos usando np.meshgrid()
    
    • Predice las clases sobre la malla utilizando: 
        Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        
        
k) Representa gráficamente:
    • La superficie de decisión usando plt.contourf()
    
    • Los puntos reales del dataset usando plt.scatter()
    
    • Añade etiquetas a los ejes con plt.xlabel() y plt.ylabel()
    
    • Añade un título con plt.title()
    
    • Muestra la figura con plt.show()
'''


# H) VALIDACION CRUZADA

cv_accuracy = cross_val_score(modelo, X_scaled, Y, cv=5, scoring='accuracy')

print(f"\n Vector de precisiones (cada pliegue): \n {cv_accuracy}")

precisionMedia= np.mean(cv_accuracy)

print(f"\n PRECISION MEDIA: \n {precisionMedia}")




# I FRONTERA de DECISION (sobre el escalado (standarScaler) del X_scaled)

x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1


y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1


    #  MALLA DE PUNTOS
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))

    # PREDICCION CLASES sobre malla 
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
 


# K) GRAFICOS

plt.contourf(xx,yy,Z, alpha=0.3)

plt.scatter(X_scaled[:,0],
            X_scaled[:,1],
            c=Y)

plt.xlabel('Sépalo largo')
plt.ylabel('Sépalo ancho')
plt.title('REGRESIÓN LOGÍSTICA: VALIDACIÓN CRUZADA')

plt.show()




# %% EJERCICIO 29

'''
29 Clasificación de tumores de cáncer de mama utilizando Regresión Logística 
    con todas las características
    
    En este ejercicio vas a construir un modelo de clasificación binaria para 
    predecir si un tumor de mama es benigno o maligno utilizando todas las 
    características disponibles en el dataset de cáncer de mama de scikit-learn.
    Dividirás los datos en conjuntos de entrenamiento y prueba, estandarizarás
    las características para mejorar el rendimiento del modelo, y evaluarás 
    la calidad del clasificador mediante múltiples métricas incluyendo accuracy,
    precision, sensibilidad, F1-score y la matriz de confusión.
    
    
    a) Importa las bibliotecas necesarias: pandas como pd, load_breast_cancer
    desde sklearn.datasets, train_test_split desde sklearn.model_selection, 
    LogisticRegression desde sklearn.linear_model, 
    StandardScaler desde sklearn.preprocessing, 
    y las métricas confusion_matrix, accuracy_score, 
    precision_score, recall_score y f1_score desde sklearn.metrics.
    
    
    b) Carga el conjunto de datos de cáncer de mama en una variable
    llamada datosCancer utilizando load_breast_cancer(). 
    Este dataset contiene mediciones de características 
    de núcleos celulares presentes en imágenes de biopsias de mama.
    
    
    c) Crea un DataFrame llamado dfCancer con todas las características
    utilizando datosCancer.data como datos y datosCancer.feature_names
    como nombres de columnas. 
    Añade una nueva columna llamada 'target' al DataFrame asignándole
    los valores de datosCancer.target, donde 0 representa tumores malignos
    y 1 representa tumores benignos.
    
    
    
    d) Análisis del dataset
    
    •	 Muestra por pantalla los nombres de todas las características
    del dataset usando datosCancer.feature_names.
    ¿Cuántas características tiene el dataset?
    

    •	Muestra los nombres de las clases objetivo con datosCancer.target_names.
    ¿Qué valor numérico corresponde a cada clase según lo que viste en el enunciado?
    
    
    •	Muestra las primeras 5 filas del dataset en formato array con 
    datosCancer.data[:5] para hacerte una idea de los valores numéricos que contiene.
    
    
    •	Una vez creado el DataFrame dfCancer (apartado c), 
    muestra sus primeras filas con .head() y consulta su estructura con .info()
    o .describe(). ¿Qué tipo de datos contiene? ¿Hay valores nulos?
    
    
    •	Muestra cuántos tumores malignos (0) y cuántos benignos (1)
    hay en el dataset usando .value_counts() sobre la columna target. 
    ¿Está el dataset balanceado?
    
'''
# a)
import pandas as pd

from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# b) CARGAR DATOS
datosCancer= load_breast_cancer()


#  c) DATAFRAME - OBJETIVO
dfCancer = pd.DataFrame(datosCancer.data,
                        columns=datosCancer.feature_names)


dfCancer['target']=datosCancer.target
# print(dfCancer['target'])

# d) ANÁLISIS del DATASET

# • Nombres de las características y cantidad
print("Nombres de las características:")
print(datosCancer.feature_names)
print(f"\nEl dataset tiene {len(datosCancer.feature_names)} características.")


# • Nombres de las clases objetivo y valores numéricos
print(f"\nClases objetivo: {datosCancer.target_names}")
# En este dataset: 0 corresponde a 'malignant' y 1 a 'benign'


# • Primeras 5 filas en formato array
print("\nPrimeras 5 filas (array):")
print(datosCancer.data[:5])


# • Visualización del DataFrame y estructura
print("\nPrimeras filas del DataFrame:")
print(dfCancer.head())


print("\nInformación del DataFrame:")
dfCancer.info()

print("\nEstadísticas descriptivas:")
print(dfCancer.describe())

# • Conteo de clases (0 = maligno, 1 = benigno)
conteo_clases = dfCancer['target'].value_counts()
print("\nConteo de tipos de tumor:")
print(conteo_clases)




# PARTE 29 B

'''
e) Selecciona las variables predictoras creando la variable X que contenga 
    todas las características del dataset usando dfCancer[datosCancer.feature_names]. 
    Crea la variable y que contenga la columna objetivo con dfCancer['target'],
    representando la clasificación benigno/maligno del tumor.
    
f) Divide el conjunto de datos en entrenamiento y prueba utilizando 
    train_test_split() con X, y como entrada y los parámetros test_size=0.2 
    y random_state=42.
    
g) Estandariza los datos creando una instancia de StandardScaler() llamada scaler.
    Ajusta el escalador con los datos de entrenamiento y transfórmalos guardando
    el resultado en X_train_scaled usando scaler.fit_transform(X_train).
    Transforma el conjunto de prueba guardando el resultado en X_test_scaled
    usando scaler.transform(X_test). La estandarización es crucial en regresión 
    logística para que todas las características contribuyan equitativamente al modelo.
    
    
h) Crea el modelo de Regresión Logística en una variable llamada modelo
    utilizando LogisticRegression(). Entrena el modelo con los datos de
    entrenamiento estandarizados usando modelo.fit(X_train_scaled, y_train).
    
i) Realiza predicciones sobre el conjunto de prueba utilizando modelo.predict(X_test_scaled)
    y guarda el resultado en la variable y_pred.
    
j) Evalúa la calidad del modelo calculando múltiples métricas de clasificación. 
    Calcula el accuracy usando accuracy_score(y_test, y_pred), la precision 
    usando precision_score(y_test, y_pred), la sensibilidad (recall) usando
    recall_score(y_test, y_pred), y el F1-score usando f1_score(y_test, y_pred).
    Calcula también la matriz de confusión usando confusion_matrix(y_test, y_pred)
    y guárdala en confusionMatrix.
    
k) Muestra por pantalla todas las métricas calculadas: accuracy, precision, 
    sensibilidad y F1-score con sus respectivas etiquetas. Finalmente, 
    muestra la matriz de confusión con un encabezado descriptivo que indique 
    claramente qué métrica se está presentando.
'''

# e) VARIABLES PREDICTORAS Y OBJETIVO
X = dfCancer[datosCancer.feature_names]
y = dfCancer['target']


# f) TRAIN TEST SPLIT | División del conjunto de datos (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(
                                                    X, 
                                                    y,
                                                    test_size=0.2, 
                                                    random_state=42)


# g) ESTANDARIZACIÓN 
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# h) MODELO (Creación y entrenamiento)
modelo = LogisticRegression()

modelo.fit(X_train_scaled, y_train)


# i) PREDICCIONES sobre el conjunto de prueba
y_pred = modelo.predict(X_test_scaled)



# j) EVALUACIÓN de la CALIDAD del modelo

    # EXACTITUD
accuracy = accuracy_score(y_test, y_pred)

    # PRECICSION
precision = precision_score(y_test, y_pred)

    # SENSIBILIDAD
sensibilidad = recall_score(y_test, y_pred)

    # F1_SCORE
f1 = f1_score(y_test, y_pred)

    # MATRIZ DE CONFUSIÓN
confusionMatrix = confusion_matrix(y_test, y_pred)



# K)  MÉTRICAS y MATRIZ DE CONFUSIÓN
print("\n*** MÉTRICAS DE CLASIFICACIÓN ***\n---------------------------------")
print(f"Accuracy (Exactitud):    {accuracy:.4f}\n")
print(f"Precision (Precisión):  {precision:.4f}\n")
print(f"Sensibilidad (Recall):   {sensibilidad:.4f}\n")
print(f"F1-Score:               {f1:.4f}\n")


print("\n*** MATRIZ DE CONFUSIÓN ***\n-------------------------")
print(confusionMatrix) 



# %% EJERCICIO 30

'''
30 En este ejercicio vas a construir un modelo de clasificación supervisada 
    utilizando el dataset de cáncer de mama de scikit-learn. A diferencia de 
    realizar una única división en entrenamiento y prueba, evaluarás el modelo
    mediante validación cruzada con 5 pliegues para obtener una estimación más 
    robusta de su rendimiento utilizando únicamente dos características del dataset.
    
    
    a) Importa las bibliotecas necesarias: numpy como np, pandas como pd, 
    load_breast_cancer desde sklearn.datasets, cross_val_score desde sklearn.model_selection,
    SVC desde sklearn.svm y StandardScaler desde sklearn.preprocessing.
    
    b) Carga el dataset de cáncer de mama en una variable llamada datosCancer
    utilizando load_breast_cancer(). A continuación, crea un DataFrame llamado 
    dfCancer con las variables predictoras usando datosCancer.data y los nombres
    de columnas usando datosCancer.feature_names. Después añade una nueva columna
    llamada 'target' con los valores de datosCancer.target.
    
    
    c) Crea un array llamado caracteristicas que contenga las siguientes
    dos variables independientes: 'mean radius' y 'mean texture'.
    Estas serán las únicas características que utilizarás para entrenar el modelo.


    d) Separa el conjunto de datos en la variable X que contenga dfCancer[caracteristicas]
    y la variable y que contenga dfCancer['target'].
    
    
    e) Aplica una normalización a los datos utilizando StandardScaler(). 
        Crea una instancia llamada scaler, y luego ajusta y transforma todos 
        los datos usando X_scaled = scaler.fit_transform(X).
        
        
    f) Crea la variable modelo como una instancia de SVC(), que representa una 
    Máquina de Vectores de Soporte con kernel por defecto.
    
    
    g) Realiza una validación cruzada con 5 pliegues utilizando cross_val_score()
    pasando como argumentos el modelo, los datos escalados X_scaled, la variable objetivo y,
    el parámetro cv=5 y scoring='accuracy'. Guarda el resultado en la variable accuracyModelo.
    
    
    h) Muestra por pantalla los resultados de la precisión obtenida en cada
    uno de los 5 pliegues utilizando un bucle for con enumerate() que imprima
    el número de iteración y la precisión correspondiente con un formato legible.
    
'''


# a) BIBLIOTECAS

import numpy as np

import pandas as pd

from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import cross_val_score

from sklearn.svm import SVC

from sklearn.preprocessing import StandardScaler

# from sklearn.model_selection import train_test_split

# from sklearn.linear_model import LogisticRegression

# from sklearn.metrics import (
#     confusion_matrix,
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score
# )


datosCancer = load_breast_cancer()

dfCancer= pd.DataFrame(datosCancer.data,
                       columns=datosCancer.feature_names)

dfCancer['target']=datosCancer.target

# c)
caracteristicas =['mean radius','mean texture']



# d) X e y
X= dfCancer[caracteristicas]

y= dfCancer['target']



# e) NORMALIZACION

scaler= StandardScaler()

X_scaled = scaler.fit_transform(X)



# f) SVC -modelo
modelo = SVC()


# g) VALIDACION CRUZADA
#  cv --> pliegues
accuracyModelo = cross_val_score(modelo, X_scaled, y, cv=5, scoring='accuracy')


# h)
for i, precision in enumerate(accuracyModelo, start=1):
    print(f"i {i}: Precisión = {precision: .2f}")
    
    
    
# %% EJERCICIO 32

'''
32 Clasificación de valoraciones de reseñas utilizando K-Nearest Neighbors (KNN)
    En este ejercicio vas a construir un modelo de clasificación supervisada
    para predecir la puntuación en estrellas (Star Rating) de reseñas basándote 
    en características textuales como el número de palabras y el valor de sentimiento. 
    Utilizarás el algoritmo K-Nearest Neighbors (KNN), dividirás los datos en 
    conjuntos de entrenamiento y prueba, normalizarás las características y 
    evaluarás el rendimiento del modelo mediante diferentes métricas de clasificación.
    
        
    a) Importa las bibliotecas necesarias: pandas como pd, train_test_split 
    desde sklearn.model_selection, StandardScaler desde sklearn.preprocessing,
    KNeighborsClassifier desde sklearn.neighbors, y las métricas accuracy_score,
    classification_report y confusion_matrix desde sklearn.metrics.
    
    b) Carga el archivo CSV llamado 'reviews_sentiment.csv' en un DataFrame
    llamado df utilizando pd.read_csv() con los parámetros delimiter=';' 
    y encoding='utf-8'. Este dataset contiene información sobre reseñas de productos 
    incluyendo el número de palabras, el valor de sentimiento y la puntuación en estrellas.
    
    c) Selecciona las columnas que servirán como características predictoras
    creando la variable features que contenga las columnas 'wordcount' y 'sentimentValue'
    del DataFrame. Luego crea la variable target que contenga la columna 'Star Rating',
    que representa la puntuación que se quiere predecir.
    
    d) Divide el conjunto de datos en conjuntos de entrenamiento y prueba 
    utilizando train_test_split() con features y target como entrada, y los
    parámetros test_size=0.2 y random_state=42.
    
    
    e) Normaliza los datos creando una instancia de StandardScaler() llamada scaler.
    Ajusta el escalador con los datos de entrenamiento y transfórmalos guardando
    el resultado en escalarAjustarEntrenamiento mediante scaler.fit_transform(X_train).
    A continuación, transforma el conjunto de prueba guardando 
    el resultado en escalarAjustarPrueba usando el método .transform(X_test).
    
    
    f) Crea el modelo K-Nearest Neighbors en una variable llamada modeloKnn 
    utilizando KNeighborsClassifier() con el parámetro n_neighbors=5, que 
    indica que el modelo considerará los 5 vecinos más cercanos para realizar
    la clasificación. Puedes ajustar este número según sea necesario para mejorar
    el rendimiento.
    
    
    g) Entrena el modelo utilizando modeloKnn.fit() con los datos de entrenamiento
    escalados escalarAjustarEntrenamiento y las etiquetas y_train.
    
    
    h) Realiza las predicciones sobre el conjunto de prueba utilizando
    modeloKnn.predict(escalarAjustarPrueba) y guarda el resultado en la variable
    prediccionesConjuntoPrueba.
    
    
    i) Evalúa el rendimiento del modelo calculando la precisión (accuracy)
    mediante accuracy_score(y_test, prediccionesConjuntoPrueba) y
    guárdala en precisionAccuracy. Calcula la matriz de confusión usando
    confusion_matrix(y_test, prediccionesConjuntoPrueba) y
    guárdala en matrizConfusion. Genera el informe de clasificación 
    completo utilizando classification_report(y_test, prediccionesConjuntoPrueba)
    y guárdalo en classification_rep.
    
    
    j) Muestra por pantalla la precisión del modelo, la matriz de confusión
    con un encabezado descriptivo, y el informe de clasificación completo que
    incluye métricas como precision, recall y f1-score para cada clase de puntuación.

'''

# a)

import pandas as pd

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
 
from sklearn.neighbors import KNeighborsClassifier

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    classification_report,
    f1_score
)


# b)
# ruta = r"C:\Users\Mañana\OneDrive - Consejería de Educación\Documentos\rm\SAA_MIA\u03_apredizajeSupervisado\ejercicios\datasets\reviews_sentiment.csv"

ruta= ( 
       r"C:\Users\Mañana\OneDrive - Consejería de Educación\Documentos\rm"
       r"\SAA_MIA\u03_apredizajeSupervisado\ejercicios\datasets\reviews_sentiment.csv"
    )

df=pd.read_csv(ruta, delimiter=';',encoding='utf-8')

print(df.head())


# C)
    # Variables predictoras - caracteristicas
features = df[['wordcount', 'sentimentValue']]

    # Variable objetivo
target = df['Star Rating']



# D) TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)


# E) STANDAR SCALER
scaler=StandardScaler()

escalarAjustarEntrenamiento= scaler.fit_transform(X_train)

escalarAjustarPrueba = scaler.transform(X_test)



# F) CREAR MODELO KNN
modeloKnn=KNeighborsClassifier(n_neighbors=5)



# G) ENTRENAR MODELO KNN
modeloKnn.fit(escalarAjustarEntrenamiento, y_train)
 
 
# H) PREDICCIÓN
prediccionesConjuntoPrueba= modeloKnn.predict(escalarAjustarPrueba)


# I) EVALUACION

    # PRECISION (accuracy)
precisionAccuracy= accuracy_score(y_test, prediccionesConjuntoPrueba)

    # MATRIZ CONFUSION
matrizConfusion = confusion_matrix(y_test, prediccionesConjuntoPrueba)

    # INFORME CLASIFICACION
classification_rep= classification_report(y_test, prediccionesConjuntoPrueba)

# f1 = f1_score(y_test, prediccionesConjuntoPrueba, average='weighted')





# J) IMPRESIÓN x pantalla
print("\n*** MÉTRICAS DE CLASIFICACIÓN ***\n---------------------------------")
print(f"Accuracy (precisión):    {precisionAccuracy:.4f}\n")

# print(f"F1-Score: {f1:.4f}\n")



print("\n*** MATRIZ DE CONFUSIÓN ***\n-------------------------")
print(matrizConfusion) 



print("\n*** INFORME DE CLASIFICACIÓN ***\n---------------------------------")
# INFORME DE CLASIFICACIÓN  -->  precision    recall  f1-score   support
print(classification_rep)



# %% EJERCICIO 33

'''
33 Comparación de estrategias de ponderación en K-Nearest Neighbors para regresión

    En este ejercicio vas a construir y comparar dos modelos de regresión utilizando
    el algoritmo K-Nearest Neighbors (KNN) con diferentes estrategias de ponderación.
    Generarás datos sintéticos basados en la función seno con ruido añadido,
    entrenarás dos modelos KNN (uno con pesos uniformes y otro con pesos basados
     en distancia), y visualizarás gráficamente 
    las diferencias entre ambas estrategias para observar cómo influyen en las predicciones.
    
    
    a) Importa las bibliotecas necesarias: numpy como np, matplotlib.pyplot como plt,
    y KNeighborsRegressor desde sklearn.neighbors.
     
    
    b) Genera los datos de entrenamiento estableciendo primero una semilla aleatoria
    con np.random.seed(0) para reproducibilidad. Crea la variable X generando 40 
    valores aleatorios entre 0 y 5 usando np.sort(5 * np.random.rand(40, 1), axis=0) 
    para mantenerlos ordenados. Genera la variable y aplicando la función seno a X
    mediante np.sin(X).ravel(). Añade ruido a algunos puntos de y modificando cada 
    quinto elemento con y[::5] += 1 * (0.5 - np.random.rand(8)) para simular datos 
    reales con irregularidades.
     
    c) Genera un conjunto de datos de prueba llamado conjuntoPrueba creando
    500 puntos equiespaciados entre 0 y 5 utilizando np.linspace(0, 5, 500)[:, np.newaxis].
    Este conjunto servirá para visualizar las predicciones del modelo de forma continua.
    
     

    d) Crea dos modelos de regresión KNN con diferentes estrategias de ponderación. 
    El primero, llamado modeloUniform, debe usar KNeighborsRegressor() con n_neighbors=5 
    y weights='uniform', donde todos los vecinos tienen el mismo peso. 
    El segundo, llamado modeloDistance, debe usar los mismos parámetros
    excepto weights='distance', donde los vecinos más cercanos tienen 
    mayor influencia en la predicción.
    
     
    e) Ajusta ambos modelos a los datos de entrenamiento utilizando modeloUniform.fit(X, y)
    y modeloDistance.fit(X, y).
     
    f) Realiza predicciones sobre el conjunto de prueba para ambos modelos. 
    Guarda las predicciones del modelo con pesos uniformes en prediccionUniform 
    usando modeloUniform.predict(conjuntoPrueba), y las predicciones del modelo
    con pesos basados en distancia en prediccionDistance usando modeloDistance.predict(conjuntoPrueba).
     
    g) Visualiza los resultados creando una figura de tamaño (12, 6)
    con plt.figure(figsize=(12, 6)). Representa los datos de entrenamiento
    como puntos de dispersión usando plt.scatter() con color 'darkorange' 
    y etiqueta 'Datos de entrenamiento'. Dibuja las predicciones 
    del modelo uniforme con plt.plot() usando color 'blue' y etiqueta 'Predicciones Uniform', 
    y las predicciones del modelo con pesos por distancia con color 'green'
    y etiqueta 'Predicciones Distance'.
    
     
    h) Añade etiquetas a los ejes usando plt.xlabel('X') y plt.ylabel('y'),
    un título descriptivo con plt.title('Regresión con K vecinos más próximos'),
    muestra la leyenda con plt.legend(), y finalmente visualiza el gráfico con plt.show().

'''


# a)

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsRegressor

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
 
from sklearn.neighbors import KNeighborsClassifier

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    classification_report,
    f1_score
)


# b) ALEATORIO

    # semilla (para que nº aleatroios siempre sean los mismos)
np.random.seed(0)

    # X --> variable independiente (datos de entradas - caracteristicas)
X= np.sort(5 * np.random.rand(40, 1), axis=0) 

    # y --> variable dependiente (salida que queremos predecir)
y= np.sin(X).ravel()


    # ruido (para wue la curva no sea perfecta)
y[::5] += 1 * (0.5 - np.random.rand(8))


# C) CONJUNTO de PRUEBA (500 puntos espaciados entre 0 y 5)
conjuntoPrueba = np.linspace(0, 5, 500)[:, np.newaxis]




# D) MODELO KNN
# se define el modelo, el cual aprende de los 5 puntos vecinos más próximos

# weights='uniform' --> todos los puntos vecinos valen lo mismo
# weights='distance' --> Cuanto más cerca, más valor tienen

modeloUniform= KNeighborsRegressor(n_neighbors=5 , weights='uniform')

modeloDistance= KNeighborsRegressor(n_neighbors=5 , weights='distance')



#  E) ENTRENAMIENTO
modeloUniform.fit(X, y)

modeloDistance.fit(X, y)


# F) PREDICCIONES
prediccionUniform= modeloUniform.predict(conjuntoPrueba)

prediccionDistance = modeloDistance.predict(conjuntoPrueba)


# G) VISUALIZACIÓN

plt.figure(figsize=(12, 6))

    # scatter --> gráfica de dispersión (puntos individuales, sin unión)
        # datos que conocemos
plt.scatter(X, y, color='darkorange', label='Datos de entrenamiento')


    # plot --> gráfica de linea (puntos conectados por una linea) una linea
        # predicción
plt.plot(conjuntoPrueba, prediccionUniform, color='blue', label='Predicciones Uniform')

plt.plot(conjuntoPrueba, prediccionDistance, color='green', label='Predicciones Distance')


plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión con K vecinos más próximos')

plt.legend()

plt.show()




'''
# ejercicio 27

plt.scatter(escalaAjusteEntrenamiento[:, 0], 
            escalaAjusteEntrenamiento[:, 1], 
            c=Y_train, 
            edgecolors='k', 
            cmap='viridis')


plt.xlabel('Sepal length (estandarizado)')
plt.ylabel('Sepal width (estandarizado)')
plt.title('Fronteras de Decisión: Regresión Logística (Iris)')
'''



# %% EJERCICIO 34

'''
34 Comparación de Árboles de Decisión con y sin limitación de profundidad
    En este ejercicio vas a construir y comparar dos modelos de clasificación 
    utilizando árboles de decisión con diferentes configuraciones. Utilizarás
    el dataset Iris de scikit-learn para entrenar un árbol de decisión con 
    profundidad máxima limitada y otro sin restricciones, y visualizarás 
    gráficamente ambos árboles para comparar su complejidad y estructura,
    observando cómo la profundidad afecta al overfitting y la interpretabilidad del modelo.
    
    
    a) Importa las librerías necesarias: load_iris desde sklearn.datasets,
    train_test_split desde sklearn.model_selection, DecisionTreeClassifier 
    desde sklearn.tree, tree desde sklearn, y matplotlib.pyplot como plt.
    
    
    b) Carga el conjunto de datos Iris en una variable llamada datosIris
    utilizando load_iris(). Extrae las características en la variable X 
    usando datosIris.data y las etiquetas en la variable y usando datosIris.target.
    
    
    c) Divide el conjunto de datos en entrenamiento y prueba utilizando 
    train_test_split() con los parámetros test_size=0.2 y random_state=42. 
    Guarda los resultados en las variables X_train, X_test, y_train, y_test.
    
    d) Crea el primer clasificador de árbol de decisión llamado arbolDepth3
    utilizando DecisionTreeClassifier() con el parámetro max_depth=3 para limitar
    la profundidad máxima del árbol a 3 niveles. Esto ayudará a prevenir el 
    sobreajuste y mantendrá el modelo más simple e interpretable. Entrena este
    clasificador utilizando arbolDepth3.fit(X_train, y_train).
    
    
    e) Crea el segundo clasificador de árbol de decisión llamado arbolSinDepth 
    utilizando DecisionTreeClassifier() sin ningún parámetro adicional,
    lo que permitirá que el árbol crezca hasta su máxima profundidad posible
    según los datos. 
    Entrena este clasificador utilizando arbolSinDepth.fit(X_train, y_train).
    

    f) Crea una figura de visualización con tamaño (25, 10) 
    usando plt.figure(figsize=(25, 10)) para mostrar ambos árboles
    lado a lado de manera clara y legible.
    
    
    g) Visualiza el primer árbol creando un subplot en la posición (1, 2, 1)
    con plt.subplot(1, 2, 1). Añade un título "Árbol de decisión con Depth=3"
    con fontsize=16. Dibuja el árbol utilizando tree.plot_tree() pasando como 
    argumentos arbolDepth3, los nombres de características 
    con feature_names=datosIris.feature_names, los nombres de clases 
    con class_names=list(datosIris.target_names), filled=True para colorear
    los nodos, fontsize=10, impurity=False para no mostrar la impureza, 
    y rounded=True para nodos redondeados. Añade una etiqueta en el eje x 
    con "Árbol con Depth=3" y fontsize=30, y un texto adicional "Depth=3" 
    centrado sobre el gráfico usando plt.text() con las coordenadas y transformación apropiadas.
    
    
    h) Visualiza el segundo árbol creando un subplot en la posición (1, 2, 2) 
    con plt.subplot(1, 2, 2). Añade un título "Árbol de decisión sin parámetros 
    adicionales" con fontsize=16. Dibuja el árbol utilizando tree.plot_tree()
    con los mismos parámetros que el árbol anterior pero pasando arbolSinDepth 
    como primer argumento. Añade una etiqueta en el eje x con "Árbol sin parámetros"
    y fontsize=30, y un texto adicional "Sin parámetros" centrado sobre el gráfico.
    
    
    i) Ajusta el espaciado entre los subplots para evitar superposiciones
    usando plt.tight_layout(), y finalmente muestra la visualización completa con plt.show().
    
'''

# a)
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt

from sklearn import tree


# b)
datosIris= load_iris()

print(datosIris.keys())
# print(datosIris.DESCR)


X= datosIris.data

y= datosIris.target


# c) TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)


# d) ARBOL DE DECISIÓN
# max_depth=3 --> Altura - profundidad  del arbol en 3
    # Si el nº es muy alto --> overfitting o sobreajuste (aprende de memoria)

arbolDepth3= DecisionTreeClassifier(max_depth=3)

arbolDepth3.fit(X_train, y_train)



# E) ARBOL DE DECISIÓN (SIN PROFUNDIDAD)

arbolSinDepth = DecisionTreeClassifier()

arbolSinDepth.fit(X_train, y_train)


# F) VISUALIZACIÓN

plt.figure(figsize=(25,10))


# G) 1er ARBOL

plt.subplot(1, 2, 1)

plt.title(label="Árbol de decisión con Depth=3", fontsize=16)

tree.plot_tree(arbolDepth3,
               feature_names=datosIris.feature_names,
               class_names=list(datosIris.target_names),
               filled=True,
               fontsize=10, 
               impurity=False,
               rounded=True)


plt.xlabel("Árbol con Depth=3",fontsize=30)

plt.text(0.5, 1.02, "Depth=3", fontsize=12)

# plt.show()



# H) 2º ARBOL

plt.subplot(1, 2, 2)

plt.title(label="Árbol de decisión sin parámetros adicionales", fontsize=16)

tree.plot_tree(arbolSinDepth,
               feature_names=datosIris.feature_names,
               class_names=list(datosIris.target_names),
               filled=True,
               fontsize=10, 
               impurity=False,
               rounded=True)


plt.xlabel("Árbol sin parámetros",fontsize=30)

plt.text(0.5, 1.02, "Sin parámetros", fontsize=12)


# I) Ajustar automáticamente el espaciado

plt.tight_layout()

plt.show()
