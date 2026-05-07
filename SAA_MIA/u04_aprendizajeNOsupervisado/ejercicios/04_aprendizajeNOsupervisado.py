# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:15:18 2026

@author: Mañana
"""
import numpy as np

import pandas as pd

from sklearn.preprocessing import StandardScaler

df=pd.read_csv('SMALL.csv')

#  a BINARIO
y = pd.get_dummies(df.SHAPE, prefix='SHAPE')

# seleccionar columnas con datos numericos
df_2=df[['TIME','STROKE','MSE','SSE','CERR']]

# STANDARD SCALER
estandarizador = StandardScaler()

df_std_2=estandarizador.fit_transform(df_2)



#  COLUMNAS BINARIAS de SHAPE
SHAPE_0 = y['SHAPE_0']
SHAPE_1 = y['SHAPE_1']
SHAPE_2 = y['SHAPE_2']
SHAPE_3 = y['SHAPE_3']


# Crear DATAFRAME
df_std=pd.DataFrame({
                    'TIME': df_std_2[:,0],
                    'STROKE': df_std_2[:,1],
                    'MSE': df_std_2[:,2],
                    'SSE': df_std_2[:,3],
                    'CERR': df_std_2[:,4],
                    'SHAPE_0' : SHAPE_0,
                    'SHAPE_1' : SHAPE_1,
                    'SHAPE_2' : SHAPE_2,
                    'SHAPE_3' : SHAPE_3
                    })

print(df_std)


# SHAPE INVERTIDO (pregunat examen)
shapeInvertido = [2,2,0,3,2,1,0,3,3,3]



# MATRIZ COVARIANZA
    # rowvar --> Si es false, la variable es la columna, no la fila
covarianza = np.cov(df_std_2, rowvar=False)


# VALORES PROPIOS y VECTORES PROPIOS
'''
    valores propios --> Array de 5 nºs (uno por dimension)
        indican cuanta varianza registra el analisis de cada componente principal (PCA)
    
    vectores propios --> matriz (5x5) donde cada columna es un vector propio
    
    vector propio --> direccion de un componente principal
    
    R3 -> 3 dimensiones (3 vectores propios)
    
    .T --> matriz traspuesta  --> cambiar filas x columnas (la diagonal queda =)
    
'''
valores_propios, vectores_propios = np.linalg.eig(covarianza)

vectores_propios = vectores_propios.T


#  OBTENER COMPONENTES POR VALORES PROPIOS
'''
     arg= argumentos y sort = ordenar
     devuelve los indices atiguos de los elementos ordenados
    
     [::-1] --> orden inverso (descendete, de mayor a menor)
'''
   
componentes_ordenados = np.argsort(valores_propios)[::-1]



# MATRIZ DE PROYECCIÓN y nuevo ESPACIO de VARIABLES
    #  todas las filas y de las columnas las 10 primeras
    
'''
    array[inicio:fin:paso]
    [:10] inicio 0, fin 10, paso sin especificar (ordenador ascedente(0,1,2,3,etc))
'''
    
matriz_proyeccion = vectores_propios[:,componentes_ordenados[:10]]

X_t= np.dot(df_std_2, matriz_proyeccion)

print(X_t)


# %% EJERCICIO 2


import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

df_datos= pd.read_csv("advertising.csv")

df_estandarizado = pd.DataFrame(
    StandardScaler().fit_transform(df_datos[['Age','Area Income']]),
    columns=['Age','Area Income']
    )


# PCA

pca= PCA()

df_rotado =pd.DataFrame(
    pca.fit_transform(df_estandarizado),
    columns=['Negro','Rojo']
    )

valores = pca.explained_variance_

vectores =pca.components_

v1, v2 = vectores[:,0],vectores[:,1]

print("Matriz de Covariazna: \n",pca.get_covariance())
print("Valores propios: \n",valores)
print("Vectores propios",vectores)
print(f"Valor 1: {valores[0]}\nVector 1: {v1}")
print(f"Valor 2: {valores[1]} \nVector 2: {v2}")

# parte B

import matplotlib.pyplot as pl

# --- Visualización: 4 subplots ---
fig, axes = pl.subplots(2, 2, figsize=(8, 8))

# 1. Datos originales
ax = axes[0, 0]
ax.set_title("Datos Originales")
ax.set_xlabel('Age'); ax.set_ylabel('Area Income')
ax.scatter(df_datos['Age'], df_datos['Area Income'], color='yellow')



# 2. Datos estandarizados
ax = axes[0, 1]
ax.set_title("Datos Estandarizados")
ax.set_xlabel('Age'); ax.set_ylabel('Area Income')
ax.scatter(df_estandarizado['Age'], df_estandarizado['Area Income'], color='yellow')



# 3. Datos estandarizados + vectores propios
ax = axes[1, 0]
ax.set_title("Datos Estandarizados con Vectores Propios")
ax.set_xlabel('Age'); ax.set_ylabel('Area Income')
ax.scatter(df_estandarizado['Age'], df_estandarizado['Area Income'], color='yellow')


qargs = dict(scale=1, scale_units='xy', angles='xy')


# ** FLECHAS **
# Vector propio 1 (Negro) 
ax.quiver(0, 0, v1[0]/abs(v1[0])*valores[0], v1[1]/abs(v1[1])*valores[0], color='black', **qargs)

# Vector propio 2 (Rojo)
ax.quiver(0, 0, v2[0]/abs(v2[0])*valores[1], v2[1]/abs(v2[1])*valores[1], color='red', **qargs)




# 4. Datos rotados y proyectados
ax = axes[1, 1]
ax.set_title("Datos Estandarizados, Rotados y Proyectados")
ax.set_xlabel('Negro'); ax.set_ylabel('Rojo')

# Gráfico principal (dispersión rotada)
ax.scatter(df_rotado['Negro'], df_rotado['Rojo'], color='grey')

# Proyección en el eje X (Negro)
ax.scatter(df_rotado['Negro'], np.full(len(df_rotado), df_rotado['Rojo'].min()), color='black')

# Proyección en el eje Y (Rojo)
ax.scatter(np.full(len(df_rotado), df_rotado['Negro'].min()), df_rotado['Rojo'], color='red')

# tight_layout() --> para que no se superpongan (ajuste automatico)
pl.tight_layout()
pl.show()

# --- Nuevos datos proyectados ---
pl.figure()
pl.title("Nuevos Datos")

# Visualización unidimensional de los componentes proyectados
pl.scatter(df_rotado['Negro'], np.full(len(df_rotado), 1), color='black')
pl.scatter(df_rotado['Rojo'], np.full(len(df_rotado), 2), color='red')

pl.tight_layout()
pl.show()


# %% EJERCICIO 3 (Practicas III)

import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

# --- Carga y normalización
COLS = ['Daily Internet Usage', 'Daily Time Spent on Site']

df_datos = pd.read_csv("advertising.csv")

df_norm = pd.DataFrame(
    MinMaxScaler().fit_transform(df_datos[COLS]),
    columns=[f"{c} Normalizado" for c in COLS]
)

# --- Modelo KMeans
kmeans = KMeans(n_clusters=10, init='k-means++').fit(df_norm)

df_norm['Cluster'] = kmeans.labels_
centroides         = kmeans.cluster_centers_
inercia            = kmeans.inertia_

print(f"Inercia: {inercia:.2f}")
print(f"Centroides: {centroides}")

# -- Visualización
fig, axes = pl.subplots(1, 2, figsize=(12, 5))

# 1. Datos originales
ax = axes[0]

ax.set_title("Datos Originales")
ax.set_xlabel(COLS[0])
ax.set_ylabel(COLS[1])

# alpha --> tranparencia
ax.scatter(df_datos[COLS[0]], df_datos[COLS[1]], color='yellow',alpha=0.6)


# 2. Datos normalizados con clusters y centroides
ax = axes[1]
ax.set_title("Datos Normalizados con Clusters")
ax.set_xlabel(f"{COLS[0]} Normalizado")
ax.set_ylabel(f"{COLS[1]} Normalizado")

ax.scatter(df_norm[f"{COLS[0]} Normalizado"],
           df_norm[f"{COLS[1]} Normalizado"],
           c=df_norm['Cluster'], cmap='tab10', alpha=0.6)

ax.scatter(centroides[:, 0], centroides[:, 1],
           marker='o', color='red', s=200, label='Centroides',zorder=5)

ax.legend()

# tight_layout --> no se superponga unos labels con otros
pl.tight_layout()
pl.show()

# %% practica III ELBOW
import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

# — Carga y normalización — -------------------------------------
COLS = ['Daily Internet Usage', 'Daily Time Spent on Site']

df_datos = pd.read_csv("advertising.csv")

df_norm = pd.DataFrame(
    MinMaxScaler().fit_transform(df_datos[COLS]),
    columns=[f"{c} Normalizado" for c in COLS]
)

# — Cálculo de inercia por número de clusters (método del codo - ELBOW) —
inercias = np.array([[2, KMeans(n_clusters=2, init='k-means++').fit(df_norm).inertia_]])

for k in range(3, 20):
    inercia = KMeans(n_clusters=k, init='k-means++').fit(df_norm).inertia_
    inercias = np.vstack([inercias, [k, inercia]])

# — Visualización — -----------------------------------------
pl.figure(figsize=(8, 8))

pl.title("Inercia por Cantidad de Clusters")
pl.xlabel("Cantidad de Clusters")
pl.ylabel("Inercia")

pl.scatter(inercias[:, 0], inercias[:, 1], color='yellow')

pl.plot(inercias[:, 0], inercias[:, 1], color='gray', linestyle='--')

pl.tight_layout()
pl.show()


# %% PRACTICA III - clustering aglomerativo

import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial import distance_matrix
from scipy.spatial.distance import squareform
from scipy.cluster import hierarchy

# — Carga y estandarización ---------------------------
COLS = ['Daily Internet Usage', 'Daily Time Spent on Site']

df_datos = pd.read_csv("advertising.csv")

df_std = pd.DataFrame(
    StandardScaler().fit_transform(df_datos[COLS]),
    columns=[f"{c} Estandarizado" for c in COLS]
)

# — Modelo Agglomerative Clustering -----------------------------------
modelo = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='complete')
df_std['Cluster'] = modelo.fit_predict(df_std)


# — Dendrograma ----------------------
mat_distancias = squareform(distance_matrix(df_std, df_std))

dendrograma = hierarchy.linkage(mat_distancias, 'complete')

# — Visualización — ----------------------------------
fig, axes = pl.subplots(1, 3, figsize=(18, 5))

# 1. Datos originales
ax = axes[0]
ax.set_title("Datos Originales")
ax.set_xlabel(COLS[0]); ax.set_ylabel(COLS[1])
ax.scatter(df_datos[COLS[0]], df_datos[COLS[1]], color='yellow', alpha=0.6)

# 2. Datos estandarizados con clusters --Clasificación Jerárquica Aglomerativa---
ax = axes[1]
ax.set_title("Datos Estandarizados")
ax.set_xlabel(f"{COLS[0]} Estandarizado"); ax.set_ylabel(f"{COLS[1]} Estandarizado")
ax.scatter(df_std[f"{COLS[0]} Estandarizado"],
           df_std[f"{COLS[1]} Estandarizado"],
           c=df_std['Cluster'], cmap='tab10', alpha=0.6)

# 3. Dendrograma --------------------------------------
ax = axes[2]
ax.set_title("Dendrograma")
hierarchy.dendrogram(dendrograma, ax=ax, no_labels=True)

pl.tight_layout()
pl.show()


# --------------------------------------
# %% EJERCICIO 17

'''
17. Empleando el archivo liga.csv, crearás un modelo K-Means que permita predecir 
    la categoría (portero, defensa, medio, delantero) de un jugador.
     Usarás un modelo de aprendizaje no supervisado para agrupar jugadores de fútbol
     en diferentes categorías según sus características estadísticas utilizando
     el algoritmo K-Means. Cargarás un dataset con información de jugadores de una liga,
     realizarás un preprocesado completo de los datos, entrenarás 
     el modelo de clustering con 4 grupos y compararás las categorías predichas
     por el algoritmo con las categorías reales para evaluar la calidad de la agrupación.
 
    a) Importa las bibliotecas necesarias:
    •	import pandas as pd
    •	import warnings
    •	from sklearn.model_selection import train_test_split
    •	from sklearn.cluster import KMeans
    •	from sklearn.preprocessing import StandardScaler
    •	warnings.filterwarnings("ignore") #evita mensajes de aviso

    b) Carga el archivo CSV llamado 'liga.csv' en un DataFrame. 
    Extrae los nombres de los jugadores en un array llamado
    nombres_jugadores usando datos['Jugador'].values para poder referenciarlos posteriormente.
    
    c) Limpia el dataset eliminando las filas que contengan valores nulos o 
    vacíos con datos.dropna(). Imprime información del DataFrame para conocer
    la estructura de los datos con los que trabajarás. 
    Utiliza los métodos de head(), info(), etc.
    
    d) Separa la característica 'Jugador' del resto de las variables creando
    la variable X que contenga todas las columnas excepto 'Jugador' 
    usando datos.drop('Jugador', axis=1). Los nombres de los jugadores 
    no deben usarse como características numéricas para el clustering, 
    ya que son identificadores textuales.
    
    e) Realiza el preprocesado de datos mediante estandarización para que
    todas las características tengan la misma escala. Crea una instancia
    de StandardScaler() llamada scaler, y ajusta y transforma los datos
    usando scaler.fit_transform(X), guardando el resultado en caracteriasticas_escaladas.
    
    ---
    
    f) Genera los conjuntos de entrenamiento y prueba utilizando train_test_split()
    con las características escaladas y los nombres de jugadores como entrada, 
    y los parámetros test_size=0.2 y random_state=42.

    g) Crea el modelo de clustering en una variable llamada kmeans utilizando KMeans()
    para agrupar a los jugadores en 4 categorías diferentes, busca en la documentación 
    qué parámetro usará. Entrena el modelo con el conjunto de entrenamiento
    usando kmeans.fit(X_train).
    
    h) Predice a qué cluster pertenece cada jugador del conjunto de prueba 
    utilizando kmeans.predict(X_test) y guarda el resultado en la variable 
    predicciones. Estas predicciones asignarán a cada jugador de prueba 
    uno de los 4 clusters identificados.
    
    i) Carga las categorías reales de los jugadores desde el CSV en una 
    variable llamada categorias_reales usando datos['categoria'].values. 
    Estas categorías representan la clasificación real o esperada de cada jugador.
    
    j) Muestra por pantalla los resultados de la clasificación para cada
    jugador del conjunto de prueba mediante un bucle que recorra todos
    los elementos. Para cada jugador, imprime su nombre obtenido de nombres_test[i], 
    la categoría predicha por el modelo sumándole 1 a predicciones[i] 
    (ya que los clusters van de 0 a 3 pero las categorías reales van de 1 a 4),
    y la categoría real obtenida de categorias_reales[i]. 
    


'''

# a)

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# b)

# crear dataframe
datos=pd.read_csv('liga.csv')

# equivale a --> Y
nombres_jugadores=datos['Jugador'].values

# los 10 primeros
print(nombres_jugadores[:10])


# c)

datos=datos.dropna()

print(datos.head())
print(datos.info())


# d)

X=datos.drop('Jugador', axis=1)


# e) STANDARD SCALER
scaler=StandardScaler()

# equivale a --> X
caracteristicas_escaladas=scaler.fit_transform(X)

print(caracteristicas_escaladas)



# f) TRAIN TEST SPLIT
# \ --> para poner en varias lineas

# X --> caracteristicas
# y --> jugadores (target)

X_train, \
X_test, \
y_train, y_test= train_test_split(
    caracteristicas_escaladas,nombres_jugadores, 
    test_size=0.2,
    random_state=42)


# g) KMEANS (con X_train))
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_train)


# h) Predicción KEMANS
predicciones = kmeans.predict(X_test)


# i) CATEGORIAS REALES
categorias_reales = datos['categoria'].values


# --------------------------------------------

# j) Visualización de resultados
print("\n--- Comparativa: Predicción vs Realidad ---")
print("--------------------------------------------------")

# print(f"{'Jugador':<15} | {'Predicción':<10} | {'Real':<10}")
# print(f"{'Jugador'} | {'Predicción'} | {'Real'}")
print('Jugador | Predicción | Real')

# print("-" * 40)
print("--------------------------------------------------")

for i in range(len(predicciones)):
    # Sumamos 1 a la predicción porque los clusters van de 0-3 y las categorías de 1-4
    
    # print(f"{nombres_jugadores[i]:<15} | {predicciones[i] + 1:<10} | {categorias_reales[i]:<10}")
    print(f"{nombres_jugadores[i]} | {predicciones[i] + 1} | {categorias_reales[i]}")
    
    
# %% EJERCICIO 18

'''
    18. Repite el ejercicio anterior, pero empleando PCA para reducir 
    la dimensionalidad de modo que se conserve el 95 por ciento de la varianza.
    Para ello, añade el import de PCA de la biblioteca sklearn.decomposition.
    Tras la creación de características_escaladas, aplica PCA para reducir 
    la dimensionalidad conservando el 95% de la varianza.
    
    Crea una instancia de PCA() con el parámetro n_components=0.95, ajusta y
    transforma las características escaladas usando pca.fit_transform(caracteristicas_escaladas),
    y guarda el resultado en caracteristicas_pca.
    Muestra por pantalla el número de componentes principales seleccionados.


'''
    
from sklearn.decomposition import PCA

pca= PCA(n_components=0.95)
caracteristicas_pca= pca.fit_transform(caracteristicas_escaladas)


# n_components_ (con guion bajo _): Es el resultado real que el modelo calculó
# tras analizar tus datos (el número exacto de columnas necesarias para llegar a ese 95%).

print(f"Nº componentes principales : {pca.n_components_}")

# ORIGINALES --> df_datos.shape
# REDUCIDOS --> caracteristicas_pca.shape


# %% EJERCICIO 19

'''
    19. Empleando el archivo small.csv, crearás dos modelos 
    de clustering jerárquico aglomerativo que agrupen observaciones 
    en 2 clusters utilizando diferentes métricas de distancia (mínima y media).
    Usarás un modelo de aprendizaje no supervisado para agrupar datos según sus 
    características numéricas y categóricas. Cargarás un dataset, realizarás
    un preprocesado completo incluyendo la conversión de variables categóricas
    a formato binario y la estandarización de variables numéricas, 
    calcularás matrices de distancia, entrenarás dos modelos de clustering jerárquico
    con distintos criterios de enlace (single y average) y visualizarás 
    los resultados mediante dendrogramas para comparar ambos métodos.
    
    
        a) Importa las bibliotecas necesarias:
            •	import pandas as pd
            •	from sklearn.preprocessing import StandardScaler
            •	from scipy.spatial import distance_matrix
            •	from scipy.cluster import hierarchy
            •	import matplotlib.pyplot as plt
            •	from sklearn.cluster import AgglomerativeClustering
            
        b) Carga el archivo CSV llamado 'small.csv' en un DataFrame llamado df.
        Muestra información básica del DataFrame utilizando los métodos head(), info()
        y shape para conocer la estructura de los datos. Verifica que el dataset contenga
        al menos 10 filas; si no se cumple esta condición, muestra un mensaje de
        error indicando que el dataset es demasiado pequeño y finaliza la ejecución 
        del programa. Solo si el dataset es válido, continúa con el resto del ejercicio.
        
        c) Convierte la columna categórica 'SHAPE' a formato binario
        utilizando pd.get_dummies(df.SHAPE, prefix='SHAPE') y guarda el resultado 
        en la variable y. Esto creará nuevas columnas binarias (0 o 1) 
        para cada categoría única presente en SHAPE.
        
        d) Selecciona las columnas numéricas del dataset creando una lista 
        llamada columnas_Numericas que contenga: "TIME", "STROKE", "MSE", "SSE", "CERR".
        Estas serán las características numéricas que se estandarizarán.
        
        e) Estandariza las columnas numéricas utilizando
        StandardScaler().fit_transform(df[columnas_Numericas]) y asigna el resultado
        directamente a df[columnas_Numericas]. La estandarización es importante
        para que todas las variables tengan el mismo peso en el cálculo de distancias.
        
        f) Crea un nuevo DataFrame estandarizado llamado df_estandarizado concatenando 
        las columnas numéricas estandarizadas df[columnas_Numericas] con
        las columnas binarias y usando pd.concat([df[columnas_Numericas], y], axis=1).
        Imprime información del DataFrame para conocer la estructura de los datos
        con los que trabajarás utilizando los métodos head(), info(), etc.
        
        g) Calcula dos matrices de distancias diferentes utilizando distance_matrix().
        Crea matriz_distancias_min con el parámetro p=1 para calcular
        la distancia Manhattan (distancia mínima), y matriz_distancias_med con p=2 
        para calcular la distancia Euclidiana (distancia media). Ambas matrices 
        tomarán df_estandarizado como entrada dos veces.
        
        h) Genera un modelo de clustering jerárquico aglomerativo con distancia
        mínima creando una instancia llamada metodo_aglomerativo_min usando AgglomerativeClustering()
        con los parámetros n_clusters=2, metric='euclidean' 
        y linkage='single' (criterio de enlace simple o distancia mínima).
        Ajusta el modelo con matriz_distancias_min usando fit() y guarda el resultado
        en resultado_min. Muestra por pantalla las etiquetas de clustering obtenidas
        usando metodo_aglomerativo_min.labels_.
 
        i) Crea un modelo de clustering jerárquico aglomerativo con distancia 
        media creando una instancia llamada metodo_aglomerativo_med usando AgglomerativeClustering()
        con los parámetros n_clusters=2, metric='euclidean' y linkage='average'
        (criterio de enlace promedio o distancia media). 
        Ajusta el modelo con matriz_distancias_med usando fit() y 
        guarda el resultado en resultado_med. Muestra por pantalla las etiquetas 
        de clustering obtenidas usando metodo_aglomerativo_med.labels_.
         
        j) Visualiza el dendrograma para el método de distancia mínima creando 
        una figura de tamaño (10, 5) con plt.figure(figsize=(10, 5)).
        Añade un título "Dendograma con distancia mínima" usando plt.title(). 
        Genera el dendrograma usando :
        hierarchy.dendrogram(hierarchy.single(matriz_distancias_min),labels=df_estandarizado.index)
        y muestra la figura con plt.show().
         
        k) Visualiza el dendrograma para el método de distancia media creando 
        una nueva figura de tamaño (10, 5). Añade un título "Dendograma con distancia media".
        Genera el dendrograma usando
        hierarchy.dendrogram(hierarchy.average(matriz_distancias_med), labels=df_estandarizado.index)
        y muestra la figura con plt.show().
        Los dendrogramas permiten observar visualmente cómo se van agrupando 
        las observaciones según el criterio de distancia utilizado.

'''

# a)
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance_matrix
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering



# b)
df=pd.read_csv('SMALL.csv')

print(df.head())

print(df.info())


# Verificar que el dataset tenga al menos 10 filas
if len(df) < 10:
    print("Error: El dataset es demasiado pequeño (menos de 10 filas).")
    
else:
    print(f"Dataset válido. Registros encontrados: {df.shape[0]}")
    print(f"Dimensiones del dataset: {df.shape}")

    # c) Convertir columna categórica SHAPE a binario
    y = pd.get_dummies(df.SHAPE, prefix='SHAPE')

    # d) Seleccionar columnas numéricas
    columnas_Numericas = ["TIME", "STROKE", "MSE", "SSE", "CERR"]

    # e) Estandarizar columnas numéricas
    scaler = StandardScaler()
    df[columnas_Numericas] = scaler.fit_transform(df[columnas_Numericas])

    # f) Crear DataFrame estandarizado concatenando numéricas y binarias
    df_estandarizado = pd.concat([df[columnas_Numericas], y], axis=1)
    
    print("\n--- Información del DataFrame Estandarizado ---")
    print(df_estandarizado.head())
    df_estandarizado.info()

    # g) Calcular matrices de distancias
    # Manhattan (p=1) y Euclídea (p=2)
    matriz_distancias_min = distance_matrix(df_estandarizado, df_estandarizado, p=1)
    matriz_distancias_med = distance_matrix(df_estandarizado, df_estandarizado, p=2)

    # h) Clustering Jerárquico Aglomerativo - Distancia Mínima (Single Linkage)
    metodo_aglomerativo_min = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='single')
    resultado_min = metodo_aglomerativo_min.fit(matriz_distancias_min)
    print("\nEtiquetas (Distancia Mínima):")
    print(metodo_aglomerativo_min.labels_)

    # i) Clustering Jerárquico Aglomerativo - Distancia Media (Average Linkage)
    metodo_aglomerativo_med = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='average')
    resultado_med = metodo_aglomerativo_med.fit(matriz_distancias_med)
    print("\nEtiquetas (Distancia Media):")
    print(metodo_aglomerativo_med.labels_)

    # j) Dendrograma - Distancia Mínima
    plt.figure(figsize=(10, 5))
    plt.title("Dendrograma con distancia mínima")
    # Se usa hierarchy.single con la matriz calculada en g)
    dendrograma_min = hierarchy.dendrogram(hierarchy.single(matriz_distancias_min), labels=df_estandarizado.index)
    plt.show()

    # k) Dendrograma - Distancia Media
    plt.figure(figsize=(10, 5))
    plt.title("Dendrograma con distancia media")
    
    # Se usa hierarchy.average con la matriz calculada en g)
    dendrograma_med = hierarchy.dendrogram(hierarchy.average(matriz_distancias_med), labels=df_estandarizado.index)
    plt.show()


# %% EJERCICIO 20

'''
    20. Empleando el archivo wine.csv que contiene información sobre vinos cuya
    última característica es la clase, usarás K-Means para categorizar los vinos. 
    Cargarás el dataset, realizarás un preprocesado completo de los datos incluyendo
    la estandarización de características, aplicarás el método del codo 
    de Elbow para determinar el número óptimo de clusters de forma visual e
    interactiva, entrenarás el modelo K-Means con el número de clusters 
    seleccionado por el usuario y compararás las categorías predichas con las reales.
    
    
    a) Importa las bibliotecas necesarias:
        •	import pandas as pd
        •	import warnings
        •	from sklearn.model_selection import train_test_split
        •	from sklearn.cluster import KMeans
        •	from sklearn.preprocessing import StandardScaler
        •	import matplotlib.pyplot as plt
        •	warnings.filterwarnings("ignore") #evita mensajes de aviso
        
        
    b) Carga el archivo CSV llamado 'wine.csv' en un DataFrame llamado datos.
    Muestra información relevante del DataFrame utilizando los métodos head(),
    info() y value_counts() sobre la columna 'CLASS' para conocer la distribución 
    de las clases de vinos en el dataset.
    
    
    c) Extrae las categorías reales de los vinos en un array llamado categoriasReales
    usando datos['CLASS'].values para poder referenciarlas posteriormente 
    en la comparación con las predicciones.
    
    
    d) Limpia el dataset eliminando todas las filas que contengan valores nulos
    o vacíos utilizando datos.dropna().
    
    e) Separa la característica 'CLASS' del resto de las variables creando 
    la variable X_vinos que contenga todas las columnas excepto 'CLASS' 
    usando datos.drop('CLASS', axis=1). La columna CLASS es la variable 
    objetivo y no debe usarse como característica predictora.
    
    f) Realiza el preprocesado de datos mediante estandarización creando
    una instancia de StandardScaler() llamada scaler_vinos. Ajusta y
    transforma los datos usando scaler_vinos.fit_transform(X_vinos) y
    guarda el resultado en caracteristicas_escaladas_vinos.
    
    g) Genera los conjuntos de entrenamiento y prueba utilizando
    train_test_split() con caracteristicas_escaladas_vinos y categoriasReales 
    como entrada, y el parámetro random_state=42. Guarda los resultados
    en X_train_vinos, X_test_vinos, categorias_train_vinos, categorias_test_vinos.
    
    -
    
    h) Determina el número óptimo de clusters usando el método del codo de Elbow. 
    Crea una lista vacía llamada iteraciones para almacenar los valores de inercia.
    Solicita al usuario que introduzca un número máximo de clusters a evaluar mediante input(),
    valida que sea un número entero positivo, y conviértelo a int. 
    Itera desde 1 hasta max_clusters creando en cada iteración un
    modelo KMeans con n_clusters=i, init='k-means++' y random_state=42. 
    Ajusta cada modelo con X_test_vinos y añade su inercia (kmeans.inertia_) a la lista iteraciones.
    
    
    i) Visualiza el gráfico del codo de Elbow creando una figura de tamaño (10, 5).
    Dibuja un gráfico de línea usando plt.plot() con el rango de 
    clusters en el eje x y las iteraciones en el eje y, añadiendo marker='o'
    para mostrar los puntos. Añade etiquetas a los ejes con plt.xlabel('Número de clusters')
    y plt.ylabel('Iteración'), un título con plt.title('Codo de Elbow'),
    y muestra el gráfico con plt.show(). El punto donde el gráfico forma 
    un "codo" indica el número óptimo de clusters.
    
    
    j) Solicita al usuario que introduzca el número de clusters con el que desea
    entrenar el modelo mediante input(). Valida que sea un número entero positivo 
    y conviértelo a int guardándolo en numClusters.
    
    
    k) Entrena el modelo K-Means final creando una instancia llamada kmeans
    con n_clusters=numClusters y random_state=42. Ajusta el modelo con los datos 
    de entrenamiento usando kmeans.fit(X_train_vinos).
    
    
    l) Predice las categorías de los vinos del conjunto de prueba utilizando 
    kmeans.predict(X_test_vinos) y guarda el resultado en la variable predicciones.
    
    
    m) Muestra por pantalla los resultados mediante un bucle que recorra todas 
    las predicciones. Para cada vino, imprime su número de índice (i+1), 
    la categoría predicha por el modelo obtenida de predicciones[i], 
    y la categoría real obtenida de categoriasReales[i].
    El formato debe permitir comparar fácilmente las predicciones con la realidad.
        

'''

# a)
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
warnings.filterwarnings("ignore")


# b)

datos=pd.read_csv('wine.csv')

print('\nHEAD:')
print(datos.head())

print('\nINFO:')
print(datos.info())

print('\nVALUE COUNTS:')
print(datos.value_counts())


# c) CATEGORIA objetivo
categorias_reales = datos['CLASS'].values


# d) LIMPIAR
datosClean=datos.dropna()


# e) Todas lac columnas, excepto CLASS (columna objetivo)
X_vinos = datosClean.drop('CLASS',axis=1)


# f) STANDARD SCALER
scaler_vinos= StandardScaler()

caracteristicas_escaladas_vinos = scaler_vinos.fit_transform(X_vinos)


# g) TRAIN TEST SPLIT
# \ --> para salto linea
# train_test_split(datosEntrada, categoriaObjetivo)

X_train_vinos, X_test_vinos, categorias_train_vinos, categorias_test_vinos =\
    train_test_split(caracteristicas_escaladas_vinos,categorias_reales) 



# h) ELBOW

# validacion con --> while not max_clusters.isdigit or int(max_clusters)<=0:
   
max_clusters=input("Nº máximo de clusteres:")

while not max_clusters.isdigit() or int(max_clusters)<=0:
     max_clusters=input("Nº máximo de clusteres:")
     
max_clusters=int(max_clusters)



iteraciones=[]

# for k in range(3, 20):
#     inercia = KMeans(n_clusters=k, init='k-means++').fit(datosClean).inertia_
#     inercias = np.vstack([inercias, [k, inercia]])


# inertia --> mides la dispersion
    
for i in range(1, max_clusters + 1):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_test_vinos)
    iteraciones.append(kmeans.inertia_)



# i)
plt.figure(figsize=(10, 5))

plt.plot(range(1, max_clusters + 1), iteraciones, marker='o')

plt.xlabel('Número de clusters')
plt.ylabel('Inercia')
plt.title('Codo de Elbow')
plt.show()


# j)

# numClusters=int(input("Nº de clustere modelo kmeans:"))

numClusters=input("Nº máximo de clusteres:")

while not numClusters.isdigit() or int(numClusters)<=0:
     numClusters=input("Nº máximo de clusteres:")
     
numClusters=int(numClusters)


kmeans= KMeans(n_clusters=numClusters, random_state=42).fit(X_train_vinos)
                


# k) PREDICCION
predicciones =kmeans.predict(X_test_vinos)


# l) MOSTRAR

print('\n\nVINO | Predicción | Real')

for i in range(len(predicciones)):
    # print(f"Vino {i+1:<10} | {predicciones[i]:<10} | {categorias_reales[i]:<10}")
    print(f"Vino {i+1} | {predicciones[i]} | {categorias_reales[i]}")
    

# %% practica iii -- DBSCAN

import pandas as pd
import matplotlib.pyplot as pl
from sklearn.cluster import DBSCAN

# --- Carga de datos ---
COLS = ['Daily Internet Usage', 'Daily Time Spent on Site']

df_datos = pd.read_csv("advertising.csv")

# --- Modelo DBSCAN ---
df_datos['Cluster'] = DBSCAN(eps=4, min_samples=10).fit_predict(df_datos[COLS])

n_clusters = len(set(df_datos['Cluster'])) - (1 if -1 in df_datos['Cluster'].values else 0)
n_ruido = (df_datos['Cluster'] == -1).sum()

print(f"Clusters encontrados: {n_clusters} | Puntos de ruido: {n_ruido}")



# --- Visualización ---
fig, axes = pl.subplots(1, 2, figsize=(14, 5))



# 1. Datos originales
ax = axes[0]
ax.set_title("Datos Originales")
ax.set_xlabel(COLS[0]); ax.set_ylabel(COLS[1])
ax.scatter(df_datos[COLS[0]], df_datos[COLS[1]], color='yellow', alpha=0.6)


# 2. Datos clasificados por DBSCAN
ax = axes[1]

ax.set_title("Datos Originales Clasificados")
ax.set_xlabel(COLS[0])
ax.set_ylabel(COLS[1])

scatter = ax.scatter(df_datos[COLS[0]], df_datos[COLS[1]], 
                     c=df_datos['Cluster'], cmap='tab10', alpha=0.6)


pl.colorbar(scatter, ax=ax, label='Cluster (-1 = ruido)')

pl.tight_layout()


pl.show()


# %% practica iii -- distancio de mahanalobis

import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
from scipy.spatial import distance


# --- Carga y limpieza ---
COLS = ['Temperature', 'Weekly_Sales']
UMBRAL = 2.7

df = (pd.read_csv("walmart.csv")
      .dropna(subset=COLS)
      .reset_index(drop=True))


# --- Cálculo de distancia de Mahalanobis al centroide ---
centroide = np.array([np.mean(df[COLS], axis=0)])


df['Mahalanobis'] = distance.cdist(df[COLS], centroide, metric='mahalanobis')


# --- Detección de anomalías (distancia > umbral) ---
df['Anomalia'] = np.where(df['Mahalanobis'] > UMBRAL, -1, 1)


print(df[COLS + ['Mahalanobis', 'Anomalia']].head(10))
print(f"\nAnomalías detectadas: {(df['Anomalia'] == -1).sum()} / {len(df)}")



# --- Visualización ---
fig, ax = pl.subplots(figsize=(7, 5))

ax.set_title("Detección de Anomalías (Mahalanobis)")
ax.set_xlabel(COLS[0]); ax.set_ylabel(COLS[1])

scatter = ax.scatter(df[COLS[0]], df[COLS[1]], 
                     c=df['Anomalia'], cmap='RdYlGn', alpha=0.6,s=15,
                     label='Datos')

ax.scatter(centroide[0][0], centroide[0][1], 
           s=200, color='red', marker='*', zorder=5, label='Centroide')

pl.colorbar(scatter, ax=ax, label='1 = normal | -1 = anomalía')

ax.legend()

pl.tight_layout()

pl.show()


# %% practica iii -- BOSQUES DE AISLAMIENTO


import pandas as pd
import matplotlib.pyplot as pl
from sklearn.ensemble import IsolationForest

# —- Carga y limpieza
COLS = ['Temperature', 'Weekly_Sales']
CONTAMINACION = 0.05

df = (pd.read_csv("walmart.csv")
      .dropna(subset=COLS)
      .reset_index(drop=True))


# —- Modelo Isolation Forest
modelo = IsolationForest(contamination=CONTAMINACION)
df['Anomalia'] = modelo.fit_predict(df[COLS])

print(df[COLS + ['Anomalia']].head(10))
print(f"\nAnomalías detectadas: {(df['Anomalia'] == -1).sum()} / {len(df)}")


# —- Visualización
fig, ax = pl.subplots(figsize=(7, 5))

ax.set_title("Detección de Anomalías (Isolation Forest)")
ax.set_xlabel(COLS[0]); ax.set_ylabel(COLS[1])

scatter = ax.scatter(df[COLS[0]], df[COLS[1]],
                     c=df['Anomalia'], cmap='RdYlGn', alpha=0.6, s=15)

pl.colorbar(scatter, ax=ax, label='1 = normal | -1 = anomalía')

pl.tight_layout()
pl.show()


# %% EJERCICIO 21

'''
21. Empleando los ficheros train.csv y test.csv, que incluyen información sobre
 vinos, implementa KMeans utilizando la biblioteca scikit-learn.
 Los apartados (a, h, i, j, k) permanecen iguales al ejercicio 20.

    b) Carga los archivos CSV llamados 'train.csv' y 'test.csv' en DataFrames
    llamados train_data y test_data respectivamente (en lugar de cargar
                                                     un único archivo 'wine.csv').
    Muestra información relevante de ambos conjuntos utilizando los métodos head(),
    info() y value_counts() sobre la columna 'CLASS' para conocer la distribución 
    de las clases de vinos en cada dataset.
    
    
    c) Extrae las categorías reales de los vinos de ambos conjuntos en arrays 
    llamados categoriasReales_train usando train_data['CLASS'].values y 
    categoriasReales_test usando test_data['CLASS'].values.
    
    
    d) Limpia ambos datasets eliminando todas las filas que contengan
    valores nulos o vacíos utilizando train_data.dropna() y test_data.dropna().
    
    e) Separa la característica 'CLASS' del resto de las variables 
    en ambos conjuntos. Crea la variable X_train que contenga todas
    las columnas excepto 'CLASS' de train_data usando train_data.drop('CLASS', axis=1),
    y la variable X_test que contenga todas las columnas excepto 'CLASS'
    de test_data usando test_data.drop('CLASS', axis=1).
    
    f) Realiza el preprocesado de datos mediante estandarización independiente 
    para cada conjunto. Crea una instancia de StandardScaler() llamada scaler_train,
    ajusta y transforma los datos de entrenamiento usando scaler_train.fit_transform(X_train)
    y guarda el resultado en X_train_scaled. Crea otra instancia de StandardScaler()
    llamada scaler_test, ajusta y transforma los datos de prueba usando 
    scaler_test.fit_transform(X_test) y guarda el resultado en X_test_scaled.
    
    g) Elimina la llamada a train_test_split() ya que los conjuntos de entrenamiento
    y prueba ya vienen separados en archivos diferentes. 
    Continúa con el método del codo de Elbow usando X_train_scaled 
    (en lugar de X_test_vinos del ejercicio anterior).
    
    
    l) Muestra por pantalla los resultados del conjunto de prueba utilizando
    categoriasReales_test[i] (en lugar de categoriasReales[i]).
    

'''

# a)

train_data=pd.read_csv('train.csv')

test_data= pd.read_csv('test.csv')


print('\n TRAIN\n---------------')
print(train_data.head())

print(train_data.info())

print(train_data['CLASS'].value_counts())


print('\n TEST\n---------------')
print(train_data.head())
print(test_data.head())

print(test_data.info())

print(test_data['CLASS'].value_counts())


# %% EJERCICIO 25

'''
ej 25 DBSCAN
    25. Empleando el algoritmo DBSCAN (Density-Based Spatial Clustering of Applications with Noise),
     crea un modelo de aprendizaje automático que agrupe los clientes mayoristas 
     utilizando el archivo CSV de Kaggle "wholesale_customers_dataset.csv"
     disponible en https://www.kaggle.com/datasets/binovi/wholesale-customers-data-set
     A diferencia de K-Means, DBSCAN no requiere especificar el número de clusters
     de antemano y puede identificar puntos atípicos como ruido. Realizarás 
     un preprocesado completo de los datos, entrenarás el modelo DBSCAN con los 
     datos de entrenamiento, predecirás las categorías del conjunto de prueba y
     mapearás los clusters encontrados a las categorías originales del dataset 
     para evaluar el rendimiento del algoritmo.

        a) Importa las bibliotecas necesarias: pandas, warnings, train_test_split
            desde sklearn.model_selection, DBSCAN desde sklearn.cluster, 
            y StandardScaler desde sklearn.preprocessing. 
            Configura warnings.filterwarnings("ignore") para evitar mensajes de aviso.
        
        
        b) Carga el archivo CSV llamado 'wholesale_customers_dataset.csv' 
            en un DataFrame llamado datos. Este dataset contiene información
            sobre clientes mayoristas incluyendo sus compras anuales
            en diferentes categorías de productos.
            
                
        c) Elimina todas las filas que contengan valores nulos o 
            vacíos utilizando datos.dropna() para asegurar la calidad de los datos.
            
        
        d) Extrae los valores de la columna 'Channel' en un array
            llamado channel usando datos['Channel'].values. 
            Esta columna representa el canal de venta (Horeca o Retail)
            y será la variable objetivo para comparar con las predicciones. 
            Separa las características 'Channel' y 'Region' del resto de 
            las variables usando datos.drop(['Channel', 'Region'], axis=1),
            ya que estas columnas no deben usarse como características
            predictoras en el clustering.
        
        e) Realiza el preprocesado de datos mediante estandarización.
            Crea una instancia de StandardScaler() llamada scaler, 
            y ajusta y transforma los datos usando scaler.fit_transform(datos),
            guardando el resultado en datos_escalados. La estandarización
            es importante para que DBSCAN calcule correctamente 
            las distancias entre puntos.
            
            
        f) Genera los conjuntos de entrenamiento y prueba utilizando
            train_test_split() con datos_escalados y channel como entrada, 
            y los parámetros test_size=0.2 y random_state=42. 
            Guarda los resultados en X_train, X_test, labels_train, labels_test.


        g) Entrena el modelo DBSCAN creando una instancia con
            los parámetros eps=1.0 (radio máximo de vecindad) 
            y min_samples=10 (número mínimo de puntos para formar un cluster denso). 
            Ajusta el modelo únicamente con los datos de entrenamiento
            usando dbscan.fit(X_train).
        
        
        h) Predice los clusters del conjunto de prueba utilizando
            dbscan.fit_predict(X_test) y guarda el resultado en la variable predicciones.
            DBSCAN asignará etiquetas numéricas a cada cluster encontrado 
            y la etiqueta -1 para puntos considerados ruido.
        
        
        i) Mapea las etiquetas predichas por DBSCAN a las categorías
            originales del dataset. Crea una lista llamada prediccionesMapeadas
            donde los puntos del cluster 0 se mapean a categoría 1, 
            y los puntos considerados ruido (etiqueta -1) o de otros 
            clusters se mapean a categoría 2. Usa una comprensión de lista:
                [1 if label == 0 else 2 for label in predicciones].
        
        
        j) Muestra por pantalla los resultados mediante un bucle que
            recorra todos los registros del conjunto de prueba. Para cada registro, 
            imprime su número de índice (i+1), la categoría predicha obtenida 
            de prediccionesMapeadas[i], y la categoría real obtenida de labels_test[i]. 
            El formato debe permitir comparar fácilmente las predicciones
            con la realidad y evaluar el rendimiento del algoritmo DBSCAN.   
                
                 
'''

# a) IMPORTACIONES
import pandas as pd
import matplotlib.pyplot as pl
from sklearn.cluster import DBSCAN
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# warnings.filterwarnings("ignore")


# b) CREAR DATAFRAME
datos=pd.read_csv('wholesale_customers_dataset.csv')


# c) ELIMINAR NULOS
datos= datos.dropna()


# d) VARIABLE OBJETIVO
channel= datos['Channel'].values


datos= datos.drop(['Channel', 'Region'], axis=1)


# e) STANDARD
scaler= StandardScaler()

datos_escalados=scaler.fit_transform(datos)


# f) TRAIN TEST SPLIT
# X --> datos_escalados --> datos de entrada
# Y --> channel --> variable objetivo
X_train, X_test, labels_train, labels_test = train_test_split(datos_escalados,channel,test_size=0.2, random_state=42)


# g) ENTRENAR MODELO DBSCAN
dbscan = DBSCAN(eps=1.0, min_samples=10)

dbscan.fit(X_train)


# h) PREDICCIÓN 
# generar grupos
predicciones = dbscan.fit_predict(X_test)


# i) MAPEADO DE ETIQUETAS


# Mapeamos: Cluster 0 -> Categoría 1 | Ruido (-1) u otros clusters -> Categoría 2
# Se aplica la lógica: Cluster 0 -> 1, el resto (-1 u otros) -> 2

# por bucle con compresión
prediccionesMapeadas = [1 if label == 0 else 2 for label in predicciones]




# j) MOSTRAR RESULTADOS
print(f"{'Registro'} | {'Predicción'} | {'Categoría Real'}")

for i in range(len(labels_test)):
    # i+1 para el índice humano, prediccionesMapeadas para el resultado y labels_test para el real
    print(f"{(i+1)} | {prediccionesMapeadas[i]} | {labels_test[i]}")
    
    

# OPCION con FORMATEO en visualización

# print(f"{'Registro':<10} | {'Predicción':<12} | {'Real':<6}")
# print("-" * 35)

# for i in range(len(labels_test)):
#     # i+1 para el índice humano, prediccionesMapeadas para el resultado y labels_test para el real
#     print(f"{(i+1):<10} | Cat: {prediccionesMapeadas[i]:<8} | Cat: {labels_test[i]}")





