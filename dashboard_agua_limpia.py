
# DASHBOARD COMPLETO - AQUALIMPIA S.A.
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# CONFIGURACIÓN
st.set_page_config(
    page_title="Dashboard AquaLimpia",
    layout="wide"
)

# TÍTULO
st.title("Dashboard Exploratorio - AquaLimpia S. A.")

st.markdown("""
Análisis operacional y ambiental de plantas de tratamiento
de aguas residuales.
""")

# CARGA DE DATOS
df = pd.read_excel(
    "dataset_set_A_aguas_residuales.xlsx"
)

# PREPARACIÓN DE DATOS
df["fecha_registro"] = pd.to_datetime(
    df["fecha_registro"]
)

# Eficiencia
df["eficiencia_tratamiento"] = (
    (
        df["DBO_entrada_mg_L"] -
        df["DBO_salida_mg_L"]
    )
    /
    df["DBO_entrada_mg_L"]
) * 100

# Cumplimiento
df["estado_cumplimiento"] = (
    df["cumplimiento_norma"]
    .apply(
        lambda x:
        "Cumple"
        if x == 1
        else "No cumple"
    )
)
# SIDEBAR
st.sidebar.header("Filtros")

planta = st.sidebar.multiselect(
    "Seleccione planta",
    options=df["planta"].unique(),
    default=df["planta"].unique()
)
cumplimiento = st.sidebar.multiselect(
    "Estado cumplimiento",
    options=df["estado_cumplimiento"].unique(),
    default=df["estado_cumplimiento"].unique()
)
# Filtrar
df_filtrado = df[
    (df["planta"].isin(planta))
    &
    (df["estado_cumplimiento"].isin(cumplimiento))
]

# MÉTRICAS
st.subheader("Indicadores Generales")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "DBO salida promedio",
        round(
            df_filtrado["DBO_salida_mg_L"].mean(),
            2
        )
    )
with col2:
    st.metric(
        "Eficiencia promedio",
        round(
            df_filtrado[
                "eficiencia_tratamiento"
            ].mean(),
            2
        )
    )
with col3:
    st.metric(
        "Caudal promedio",
        round(
            df_filtrado[
                "caudal_entrada_m3_d"
            ].mean(),
            2
        )
    )
with col4:
    porcentaje = (
        df_filtrado["cumplimiento_norma"]
        .mean()
    ) * 100

    st.metric(
        "% Cumplimiento",
        round(porcentaje, 2)
    )
# GRÁFICO 1
st.subheader("Tendencia Temporal DBO Salida")
fig1 = px.line(
    df_filtrado,
    x="fecha_registro",
    y="DBO_salida_mg_L",
    color="planta",
    markers=True
)
st.plotly_chart(
    fig1,
    use_container_width=True
)
# GRÁFICO 2
st.subheader("Eficiencia Promedio por Planta")
eficiencia = (
    df_filtrado
    .groupby("planta")[
        "eficiencia_tratamiento"
    ]
    .mean()
    .reset_index()
)
fig2 = px.bar(
    eficiencia,
    x="planta",
    y="eficiencia_tratamiento",
    color="planta",
    text_auto=True
)
st.plotly_chart(
    fig2,
    use_container_width=True
)
# GRÁFICO 3
st.subheader("Caudal vs DBO Salida")
fig3 = px.scatter(
    df_filtrado,
    x="caudal_entrada_m3_d",
    y="DBO_salida_mg_L",
    color="estado_cumplimiento",
    size="energia_aeracion_kWh",
    hover_data=["planta"]
)
st.plotly_chart(
    fig3,
    use_container_width=True
)
# GRÁFICO 4
st.subheader("Consumo Energético")
fig4 = px.box(
    df_filtrado,
    x="planta",
    y="energia_aeracion_kWh",
    color="planta"
)
st.plotly_chart(
    fig4,
    use_container_width=True
)
# GRÁFICO 5
st.subheader("Lodos Generados")
lodos = (
    df_filtrado
    .groupby("planta")[
        "lodos_generados_kg_d"
    ]
    .mean()
    .reset_index()
)
fig5 = px.bar(
    lodos,
    x="planta",
    y="lodos_generados_kg_d",
    color="planta",
    text_auto=True
)

st.plotly_chart(
    fig5,
    use_container_width=True
)
# GRÁFICO 6
st.subheader("Distribución de Eficiencia")
fig6 = px.histogram(
    df_filtrado,
    x="eficiencia_tratamiento",
    nbins=20,
    color="planta"
)
st.plotly_chart(
    fig6,
    use_container_width=True
)
# GRÁFICO 7
st.subheader("Cumplimiento Normativo")
cumple = (
    df_filtrado["estado_cumplimiento"]
    .value_counts()
    .reset_index()
)
cumple.columns = [
    "Estado",
    "Cantidad"
]
fig7 = px.pie(
    cumple,
    names="Estado",
    values="Cantidad"
)
st.plotly_chart(
    fig7,
    use_container_width=True
)
# TABLA
st.subheader("Datos Filtrados")
st.dataframe(
    df_filtrado,
    use_container_width=True
)
# EXPORTAR REPORTES
st.subheader("Exportación Reportes")
# Reporte operaciones
reporte_operaciones = df_filtrado[
    [
        "fecha_registro",
        "planta",
        "caudal_entrada_m3_d",
        "DBO_entrada_mg_L",
        "DBO_salida_mg_L",
        "energia_aeracion_kWh",
        "lodos_generados_kg_d",
        "eficiencia_tratamiento"
    ]
]

# Reporte ambiental
reporte_ambiental = df_filtrado[
    [
        "fecha_registro",
        "planta",
        "DBO_salida_mg_L",
        "estado_cumplimiento"
    ]
]

# Descargar operaciones
csv1 = reporte_operaciones.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Descargar Reporte Operaciones",
    data=csv1,
    file_name="reporte_operaciones.csv",
    mime="text/csv"
)
# Descargar ambiental
csv2 = reporte_ambiental.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Descargar Reporte Ambiental",
    data=csv2,
    file_name="reporte_gestion_ambiental.csv",
    mime="text/csv"
)
# FINAL
st.markdown("---")

st.markdown("""
Dashboard desarrollado para apoyar la toma de decisiones
operacionales y ambientales en AquaLimpia S. A.
""")