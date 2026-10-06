# Smart Grid Data Analytics: Telemetría Residencial de Austin (2018)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tomasabrate/Pecan_Street_Austin_Smart_Grid/blob/main/notebooks/Pecan_Street_Austin_Smart_Grid.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/tomasabrate/pecan-street-austin-smart-grid)

Este repositorio contiene la arquitectura fundacional de datos (ETL y Análisis Exploratorio) para el procesamiento masivo de telemetría proveniente de medidores inteligentes (IoT) en el marco de redes eléctricas inteligentes (*Smart Grids*).

## 1. Problema Analítico
La volatilidad extrema de la demanda eléctrica residencial, exacerbada por picos climáticos y la adopción de energía solar, es el mayor desafío operativo para las redes eléctricas. 
*   **Objetivo:** Caracterizar los patrones de consumo a nivel de hogar individual y sentar las bases matemáticas para predecir eventos de alto estrés (anomalías o picos sostenidos).
*   **Variables Críticas:** La métrica principal analizada es `grid`, interpretada no como consumo bruto, sino como **intercambio neto con la red**. Los valores negativos son críticos ya que documentan la inyección de energía fotovoltaica al sistema.

## 2. Pipeline de Datos (Ingeniería y ETL)
Para manejar cientos de miles de registros granulares (15 minutos) de manera escalable, se implementó el siguiente flujo:
*   **Procesamiento Analítico:** Sustitución de cargas masivas en memoria por consultas SQL dinámicas utilizando **DuckDB**, permitiendo filtrar y agregar antes de interactuar con Pandas.
*   **Manejo de Nulos Semánticos:** En sistemas IoT, la ausencia de transmisión no equivale a un valor "cero". El pipeline protege la integridad evitando imputaciones ciegas.
*   **Alineación Espacio-Temporal:** Estandarización de las bases de datos en `UTC` para garantizar la continuidad matemática, con proyecciones al huso horario local (`America/Chicago`) para el descubrimiento de hábitos humanos.
*   **Enriquecimiento:** Fusión (*join*) de la serie temporal continua con los metadatos estructurales de cada vivienda (año de construcción, superficie, presencia de paneles).

## 3. Métricas y Hallazgos del EDA
El Análisis Exploratorio de Datos (EDA) funcionó como un proceso forense, demostrando que:
*   **Ausencia de un "Hogar Promedio":** La dispersión del consumo entre diferentes casas es masiva. Definir un umbral global de "alto consumo" es erróneo; el pipeline demuestra que se debe calcular un percentil P95/P99 específico por cada hogar.
*   **Estructura de Eventos Extremos:** El riesgo para la infraestructura (transformadores) no radica en picos instantáneos, sino en la persistencia del consumo máximo durante varias horas seguidas.
*   **Impacto de Variables Exógenas:** Se validó la altísima correlación entre el comportamiento horario, la época del año (estacionalidad de verano) y el intercambio neto.

---

## 📂 Acceso al Código y Notebooks

El corazón metodológico de este análisis se encuentra detallado y pre-ejecutado en el siguiente notebook. No es necesario ejecutarlo para evaluar los resultados, las tablas y conclusiones están renderizadas.

👉 **[Ver Notebook Principal: Exploración y Modelado (Pecan_Street_Austin_Smart_Grid.ipynb)](notebooks/Pecan_Street_Austin_Smart_Grid.ipynb)**

*(Nota: En la sección final del notebook se detalla el diseño propuesto para la siguiente iteración del proyecto, abarcando Feature Engineering Avanzado, estrategias de validación sin Data Leakage y despliegue MLOps).*

---

## ⚙️ Estructura del Repositorio y Reproducibilidad

El repositorio está organizado bajo estándares de ingeniería de datos para asegurar su reproducibilidad:

```text
proyecto-smart-grid-austin/
├── README.md               # Caso de estudio y resumen de ingeniería (Este documento)
├── requirements.txt        # Dependencias fijadas (pandas, duckdb, matplotlib, etc.)
├── data/
│   ├── raw/                # (No incluido en Git) Datos originales descargados de Kaggle/Pecan Street
│   └── processed/          # Artefactos analíticos intermedios
├── src/                    # Módulos Python auxiliares (transformaciones, descargas automáticas)
└── notebooks/
    └── Pecan_Street_Austin_Smart_Grid.ipynb  # Notebook con todas las celdas pre-ejecutadas
```

### Reproducción Local
1. Clona este repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`.
3. El código está diseñado con independencia de rutas (sin rutas absolutas locales). Los datos crudos requeridos deben colocarse en `data/raw/` (se recomienda usar Kaggle API para su descarga).
