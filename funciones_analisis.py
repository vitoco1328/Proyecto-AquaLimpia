import pandas as pd

# Calcular eficiencia del tratamiento
def calcular_eficiencia(df):

    df["eficiencia"] = (
        (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"])
        / df["DBO_entrada_mg_L"]
    ) * 100

    return df

# Evaluar cumplimiento normativo
def evaluar_cumplimiento(df):

    df["estado"] = df["cumplimiento_norma"].map({
        1: "Cumple",
        0: "No cumple"
    })

    return df

# Estadísticas descriptivas
def resumen_estadistico(df):

    return df.describe()