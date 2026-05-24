# Proyecto de Ciencia de Datos
# AquaLimpia S. A.
## Análisis Operacional y Ambiental de Plantas de Tratamiento de Aguas Residuales

---

# Introducción

La empresa AquaLimpia S. A. se dedica al tratamiento de aguas residuales urbanas e industriales mediante distintas plantas de tratamiento distribuidas en la región. Debido a las variaciones diarias en el caudal de entrada y en las cargas contaminantes recibidas, la organización debe mantener un control constante de sus procesos para asegurar el cumplimiento de la normativa ambiental vigente.

Durante el último trimestre, la Ing. Daniela Rojas Muñoz, jefa de Gestión Ambiental y Operaciones, detectó incumplimientos intermitentes en parámetros críticos asociados a la calidad del efluente tratado, principalmente relacionados con la Demanda Biológica de Oxígeno (DBO) y la eficiencia operacional del sistema.

Ante esta situación, se desarrolló un proyecto de análisis de datos utilizando herramientas de ciencia de datos con el objetivo de identificar patrones operacionales, analizar el desempeño de las plantas y generar información útil para apoyar la toma de decisiones técnicas, operacionales y ambientales.

El proyecto incluyó el desarrollo de un notebook analítico en Python, scripts modulares reutilizables y un dashboard interactivo en Streamlit para la visualización exploratoria de indicadores ambientales y operacionales.

---

# Objetivos del Proyecto

## Objetivo General

Analizar el comportamiento operacional y ambiental de las plantas de tratamiento de AquaLimpia S. A. mediante técnicas de análisis exploratorio de datos y visualización interactiva.

## Objetivos Específicos

- Analizar el comportamiento de variables operacionales como caudal, DBO, energía y generación de lodos.
- Evaluar el nivel de cumplimiento normativo de las plantas.
- Identificar diferencias operacionales entre plantas de tratamiento.
- Construir un dashboard interactivo para facilitar la interpretación de resultados.
- Aplicar reutilización de scripts y programación modular para mejorar la organización del proyecto.

---

# Descripción del Dataset

El dataset utilizado corresponde al archivo:

```text
dataset_set_A_aguas_residuales.xlsx
```

El conjunto de datos contiene 200 registros operacionales y ambientales asociados a distintas plantas de tratamiento.

## Variables del dataset

| Variable | Descripción |
|---|---|
| fecha_registro | Fecha del registro operacional |
| planta | Planta de tratamiento |
| caudal_entrada_m3_d | Caudal de entrada diario |
| DBO_entrada_mg_L | DBO de entrada |
| SST_entrada_mg_L | Sólidos suspendidos totales |
| pH_entrada | Nivel de pH |
| energia_aeracion_kWh | Energía utilizada en aireación |
| lodos_generados_kg_d | Lodos generados |
| DBO_salida_mg_L | DBO del efluente tratado |
| cumplimiento_norma | Cumplimiento normativo |
| eficiencia | Eficiencia del tratamiento |
| estado | Estado de cumplimiento |

---

# Exploración y Calidad de Datos

El análisis inicial permitió verificar la estructura y calidad del dataset.

## Información general del dataset

- Total de registros: 200
- Total de variables: 12
- Valores nulos: 0
- Variables numéricas: 9
- Variables categóricas: 3

## Validación de datos

No se identificaron valores nulos ni inconsistencias críticas en las variables principales del análisis.

---

# Estadísticas Descriptivas

## Indicadores Generales

| Indicador | Resultado |
|---|---|
| Caudal promedio | 5059.29 m³/d |
| DBO entrada promedio | 280.15 mg/L |
| DBO salida promedio | 36.18 mg/L |
| Eficiencia promedio | 87.09 % |
| Energía promedio | 1256.39 kWh |
| Lodos promedio | 428.80 kg/d |

---

# Resultados del Análisis

## Análisis de Eficiencia

La eficiencia promedio del sistema alcanzó un valor de 87.09%, lo que indica una capacidad importante de remoción de materia orgánica en las plantas de tratamiento.

Sin embargo, los resultados muestran diferencias operacionales entre plantas, especialmente relacionadas con el consumo energético y el caudal procesado.

---

## Cumplimiento Normativo

El análisis del indicador `cumplimiento_norma` evidenció que una parte importante de los registros presenta incumplimientos normativos relacionados con la DBO de salida.

Esto demuestra la necesidad de fortalecer el monitoreo operacional y optimizar los procesos de tratamiento para reducir riesgos regulatorios y ambientales.

---

## Análisis por Planta

| Planta | Caudal Promedio | DBO Salida | Energía | Lodos | Eficiencia |
|---|---|---|---|---|---|
| Planta Centro | 5112.72 | 35.90 | 1260.85 | 433.01 | 87.51% |
| Planta Norte | 5287.87 | 36.56 | 1299.31 | 450.47 | 86.65% |
| Planta Sur | 4684.52 | 36.06 | 1193.78 | 394.44 | 87.10% |

### Interpretación Técnica

- La Planta Norte presenta el mayor consumo energético.
- La Planta Centro procesa el mayor caudal promedio.
- La Planta Sur genera menos lodos y mantiene una eficiencia estable.
- Las diferencias operacionales sugieren variaciones en las condiciones de operación y en las cargas contaminantes recibidas.

---

# Dashboard Exploratorio

Se desarrolló un dashboard interactivo utilizando Streamlit para visualizar los principales indicadores operacionales y ambientales del sistema.

## Visualizaciones incorporadas

- Tendencia temporal de DBO de salida
- Eficiencia promedio por planta
- Relación entre caudal y DBO salida
- Consumo energético
- Generación de lodos
- Distribución de eficiencia
- Cumplimiento normativo

El dashboard permite filtrar información y explorar el comportamiento de las plantas en tiempo real.

---

# Reutilización de Scripts y Código Modular

Para mejorar la organización del proyecto se implementó programación modular mediante archivos externos reutilizables.

## Archivos utilizados

| Archivo | Función |
|---|---|
| funciones_analisis.py | Cálculos y procesamiento |
| funciones_graficos.py | Generación de gráficos |
| dashboard_aqua_limpia.py | Dashboard Streamlit |
| analisis_aguas.ipynb | Análisis exploratorio |

## Beneficios obtenidos

- Reutilización de código
- Mayor organización del proyecto
- Facilidad de mantenimiento
- Escalabilidad
- Reducción de errores
- Mejor comprensión del análisis

---

# Tecnologías Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook
- GitHub

---

# Conclusiones

El análisis desarrollado permitió comprender el comportamiento operacional y ambiental de las plantas de tratamiento de AquaLimpia S. A.

Los resultados evidenciaron que las plantas presentan una eficiencia promedio elevada, cercana al 87%, demostrando una capacidad adecuada de remoción de contaminantes. Sin embargo, también se identificaron incumplimientos normativos asociados a la DBO de salida, lo que representa un riesgo ambiental y regulatorio para la empresa.

El análisis comparativo permitió detectar diferencias entre plantas relacionadas con el caudal procesado, el consumo energético y la generación de lodos, proporcionando información relevante para la toma de decisiones operacionales y ambientales.

La implementación de programación modular y reutilización de scripts mejoró significativamente la organización del proyecto, facilitando el mantenimiento del código, la automatización de procesos y la reproducibilidad del análisis.

Finalmente, el dashboard interactivo desarrollado en Streamlit permitió visualizar de forma clara e intuitiva los principales indicadores del sistema, contribuyendo al monitoreo y evaluación continua del desempeño de las plantas de tratamiento.


