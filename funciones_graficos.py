import plotly.express as px

# 1. Tendencia temporal DBO salida
def grafico_dbo_tiempo(df):

    # ordenar por fecha
    df = df.sort_values("fecha_registro")

    fig = px.line(
        df,
        x="fecha_registro",
        y="DBO_salida_mg_L",
        color="planta",
        title="Tendencia Temporal DBO Salida",
        template="plotly_white",
        color_discrete_sequence=px.colors.sequential.Blues,
    )

    return fig
# 2. Eficiencia promedio por planta

def grafico_eficiencia(df):
    eficiencia = df.groupby("planta")["eficiencia"].mean().reset_index()
    fig = px.bar(
        eficiencia,
        x="planta",
        y="eficiencia",
        color="planta",
        title="Eficiencia Promedio por Planta",
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    return fig

# 3. Caudal vs DBO salida
def grafico_caudal_dbo(df):
    fig = px.scatter(
        df,
        x="caudal_entrada_m3_d",
        y="DBO_salida_mg_L",
        color="planta",
        size="caudal_entrada_m3_d",
        title="Caudal vs DBO Salida",
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    return fig

# 4. Consumo energético
def grafico_energia(df):
    energia = df.groupby("planta")[
        "energia_aeracion_kWh"
    ].mean().reset_index()
    fig = px.bar(
        energia,
        x="planta",
        y="energia_aeracion_kWh",
        color="planta",
        title="Consumo Energético",
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    return fig

# 5. Lodos generados
def grafico_lodos(df):
    fig = px.box(
        df,
        x="planta",
        y="lodos_generados_kg_d",
        color="planta",
        title="Lodos Generados",
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    return fig
# 6. Distribución eficiencia
def grafico_distribucion(df):
    fig = px.histogram(
        df,
        x="eficiencia",
        nbins=20,
        color="planta",
        title="Distribución de Eficiencia",
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    return fig

# 7. Cumplimiento normativo
def grafico_cumplimiento(df):
    cumplimiento = df["estado"].value_counts().reset_index()
    cumplimiento.columns = ["estado", "cantidad"]
    fig = px.pie(
        cumplimiento,
        names="estado",
        values="cantidad",
        title="Cumplimiento Normativo",
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    return fig