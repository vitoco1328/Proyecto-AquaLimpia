import streamlit as st
import pandas as pd
from funciones_analisis import *
from funciones_graficos import *
from funciones_avanzadas import (
    calcular_promedio_numpy,
    detectar_outliers,
    cargar_modelo
)
# Configuración
st.set_page_config(
    page_title="Dashboard AquaLimpia",
    layout="wide"
)
st.title("Dashboard Exploratorio - AquaLimpia S.A.")
st.markdown("""
Análisis operacional y ambiental
de plantas de tratamiento de aguas residuales.
""")

# Cargar dataset
df = pd.read_excel(
    "dataset_set_A_aguas_residuales.xlsx"
)

# Procesamiento
df = calcular_eficiencia(df)

df = evaluar_cumplimiento(df)

# Indicadores
col1, col2, col3, col4 = st.columns(4)
col1.metric(
    "DBO salida promedio",
    round(df["DBO_salida_mg_L"].mean(), 2)
)
col2.metric(
    "Eficiencia promedio",
    round(df["eficiencia"].mean(), 2)
)
col3.metric(
    "Caudal promedio",
    round(df["caudal_entrada_m3_d"].mean(), 2)
)
cumplimiento = (
    df["cumplimiento_norma"].mean()
) * 100
col4.metric(
    "% Cumplimiento",
    round(cumplimiento, 2)
)
# Filtros

planta = st.sidebar.multiselect(
    "Seleccione planta",
    options=df["planta"].unique(),
    default=df["planta"].unique()
)
df_filtrado = df[df["planta"].isin(planta)]
#Mostrar métricas avanzadas
promedio = calcular_promedio_numpy(
    df,
    "DBO_salida_mg_L"
)
st.metric(
    "Promedio DBO",
    round(promedio, 2)
)
#Mostrar cantidad de outliers
outliers = detectar_outliers(
    df,
    "DBO_salida_mg_L"
)
st.write(
    "Cantidad de valores atípicos:",
    len(outliers)
)
# Cargar modelo predictivo
modelo = cargar_modelo(
    "modelos/modelo_regresion.pkl"
)
prediccion = modelo.predict([[5000]])
st.write(
    "Predicción DBO salida:",
    round(prediccion[0], 2)
)

# Gráficos

st.plotly_chart(
    grafico_dbo_tiempo(df_filtrado),
    width="stretch"
)
st.plotly_chart(
    grafico_eficiencia(df_filtrado),
    width="stretch"
)
st.plotly_chart(
    grafico_caudal_dbo(df_filtrado),
    width="stretch"
)
st.plotly_chart(
    grafico_energia(df_filtrado),
    width="stretch"
)
st.plotly_chart(
    grafico_lodos(df_filtrado),
    width="stretch"
)
st.plotly_chart(
    grafico_distribucion(df_filtrado),
    width="stretch"
)

st.plotly_chart(
    grafico_cumplimiento(df_filtrado),
    width="stretch"
)

# Tabla
st.subheader("Datos Filtrados")
st.dataframe(df_filtrado)

# Exportación áreas
operaciones = df_filtrado[[
    "fecha_registro",
    "planta",
    "caudal_entrada_m3_d",
    "DBO_entrada_mg_L",
    "DBO_salida_mg_L",
    "energia_aeracion_kWh",
    "lodos_generados_kg_d"
]]
gestion = df_filtrado[[
    "fecha_registro",
    "planta",
    "DBO_salida_mg_L",
    "estado"
]]
operaciones.to_csv(
    "operaciones.csv",
    index=False
)
gestion.to_csv(
    "gestion_ambiental.csv",
    index=False
)
st.success("Archivos exportados correctamente")