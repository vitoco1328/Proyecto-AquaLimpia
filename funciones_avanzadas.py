import numpy as np
from scipy import stats
from joblib import dump, load
from sklearn.linear_model import LinearRegression

# FUNCIÓN 1: PROMEDIO CON NUMPY
def calcular_promedio_numpy(df, columna):
    return np.mean(df[columna])

# FUNCIÓN 2: DESVIACIÓN ESTÁNDAR
def calcular_desviacion(df, columna):
    return np.std(df[columna])

# FUNCIÓN 3: DETECCIÓN DE OUTLIERS CON SCIPY
def detectar_outliers(df, columna):
    z_scores = np.abs(stats.zscore(df[columna]))
    outliers = df[z_scores > 3]
    return outliers

# FUNCIÓN 4: MODELO PREDICTIVO SIMPLE
def entrenar_modelo(df):
    X = df[["caudal_entrada_m3_d"]]
    y = df["DBO_salida_mg_L"]
    modelo = LinearRegression()
    modelo.fit(X, y)
    return modelo

# FUNCIÓN 5: GUARDAR MODELO
def guardar_modelo(modelo, ruta):
    dump(modelo, ruta)

# FUNCIÓN 6: CARGAR MODELO
def cargar_modelo(ruta):
    return load(ruta)
