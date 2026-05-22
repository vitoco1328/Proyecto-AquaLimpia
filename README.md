# Proyecto de Ciencia de Datos - AquaLimpia S. A.

## Descripción General

Este proyecto tiene como objetivo analizar el desempeño operacional y ambiental de distintas plantas de tratamiento de aguas residuales pertenecientes a AquaLimpia S. A.

El análisis busca identificar patrones relacionados con incumplimientos en parámetros críticos de calidad del efluente, especialmente en niveles de DBO y eficiencia del tratamiento.

---

# Objetivos del Proyecto

## Objetivo General

Desarrollar un sistema analítico exploratorio que permita monitorear el comportamiento de las plantas de tratamiento y apoyar la toma de decisiones operacionales y ambientales.

## Objetivos Específicos

- Analizar tendencias de DBO de entrada y salida.
- Evaluar la eficiencia del tratamiento.
- Comparar desempeño entre plantas.
- Identificar posibles desviaciones operacionales.
- Construir un dashboard interactivo.
- Generar archivos de salida para distintas áreas de la empresa.

---

# Dataset Utilizado

Archivo:

```text
dataset_set_A_aguas_residuales.xlsx
```

Variables principales:

- Fecha de registro
- Planta de tratamiento
- Caudal de entrada
- DBO entrada
- DBO salida
- Consumo energético
- Lodos generados
- Estado de cumplimiento normativo

---

# Herramientas Utilizadas

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Git
- GitHub

---

# Flujo de Trabajo

## 1. Carga de datos

Se realizó la importación del dataset utilizando Pandas para centralizar la información en un entorno de análisis.

## 2. Limpieza y transformación

Se aplicaron procesos de:

- eliminación de duplicados,
- conversión de fechas,
- validación de datos numéricos,
- tratamiento de valores nulos.

## 3. Cálculo de indicadores

La eficiencia del tratamiento fue calculada mediante:

Eficiencia = ((DBO Entrada - DBO Salida) / DBO Entrada) * 100

## 4. Análisis exploratorio

Se desarrollaron visualizaciones para analizar:

- tendencias temporales,
- eficiencia por planta,
- relación entre caudal y DBO,
- consumo energético,
- cumplimiento normativo.

## 5. Dashboard interactivo

Se construyó un dashboard mediante Streamlit para facilitar la visualización y análisis de resultados.

---

# Dashboard Desarrollado

El dashboard incluye:

- indicadores generales,
- gráficos interactivos,
- filtros por planta,
- tablas dinámicas,
- métricas operacionales y ambientales.

Visualizaciones principales:

- Tendencia DBO salida
- Eficiencia promedio
- Caudal vs DBO salida
- Consumo energético
- Generación de lodos
- Distribución de eficiencia
- Cumplimiento normativo

---

# Archivos de Salida

## Área de Operaciones

Archivo generado:

```text
operaciones.csv
```

Incluye:

- fecha,
- planta,
- caudal,
- DBO entrada,
- DBO salida,
- consumo energético,
- lodos generados,
- eficiencia.

## Área de Gestión Ambiental

Archivo generado:

```text
gestion_ambiental.csv
```

Incluye:

- fecha,
- planta,
- DBO salida,
- cumplimiento normativo.

---

# Resultados Obtenidos

Principales resultados observados:

- DBO salida promedio: 21.77 mg/L
- Eficiencia promedio: 89.73%
- Cumplimiento normativo: 100%
- Caudal promedio: 4598.64 m³/d

El análisis permitió detectar patrones operacionales y diferencias de desempeño entre plantas de tratamiento.

---

# Control de Versiones

El proyecto fue gestionado mediante Git y GitHub para asegurar trazabilidad y respaldo de versiones.

Estructura del repositorio:

```text
Proyecto-AquaLimpia/
│
├── dashboard_agua_limpia.py
├── analisis_aguas.ipynb
├── dataset_set_A_aguas_residuales.xlsx
├── README.md
├── requirements.txt
│
├── outputs/
│   ├── operaciones.csv
│   └── gestion_ambiental.csv
```

---

# Conclusiones

La implementación del proyecto permitió transformar datos operacionales y ambientales en información útil para apoyar la toma de decisiones en AquaLimpia S. A.

El dashboard interactivo facilitó la identificación de patrones relevantes relacionados con eficiencia, DBO y cumplimiento normativo, fortaleciendo el monitoreo ambiental y operacional de las plantas de tratamiento.

Además, la documentación técnica y el control de versiones permitieron garantizar reproducibilidad, organización y trazabilidad del proyecto.