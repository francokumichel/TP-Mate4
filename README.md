# Variación Temporal de Índices de Precipitación Extrema en La Plata 🌧️📊
**Proyecto de Investigación - Matemática IV | Facultad de Informática, UNLP**

## 🎯 Descripción del Proyecto
Este estudio analiza la evolución histórica de las precipitaciones en la ciudad de La Plata (1961-2024) utilizando índices estandarizados por el ETCCDI. El trabajo no solo examina la variación temporal de estos extremos, sino que también modela la relación entre ellos mediante Regresión Lineal Múltiple. El objetivo es evaluar la capacidad explicativa conjunta de los indicadores de intensidad, frecuencia y duración sobre variables críticas como Rx1day, PRCPTOT y CWD, permitiendo identificar patrones complejos en el régimen hídrico de la región.

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.x
- **Análisis de Datos:** `Pandas`, `NumPy`
- **Estadística:** `Statsmodels`, `SciPy`
- **Visualización:** `Matplotlib`, `Seaborn`
- **Entorno:** Jupyter Notebooks (`.ipynb`)

## 📂 Estructura del Repositorio

- 📁 `data/`: Contiene los registros meteorológicos diarios utilizados (1960-2025).
- 📁 `notebooks/`: Contiene los notebooks desarrollados 
- 📓 `EDA.ipynb`: Notebook dedicado al Análisis Exploratorio de Datos, limpieza y visualización inicial de la serie temporal.
- 📓 `Analisis_PP_Extrema.ipynb`: Notebook principal donde se calculan los índices ETCCDI y se realizan los tests estadísticos de tendencia.
- 📄 `Informe_Final.pdf`: Documento detallado con la metodología, marco teórico y conclusiones del estudio.

## Cómo ejecutar el proyecto

### 1. Requisitos previos
Asegúrate de tener instalada una distribución de Python (recomendado Anaconda) o utiliza Google Colab.

### 2. Ejecución

- **Ejecutar EDA.ipynb**: Este paso es crucial para entender la distribución de los datos y validar que no existan inconsistencias en la serie de tiempo.

- **Continúa con Analisis_PP_Extrema.ipynb**: Aquí se generan las gráficas de regresión lineal y se calculan las pendientes de tendencia para cada índice.

## 📈 Conclusiones Clave

El análisis se dividió en dos fases fundamentales:

1. Análisis de Tendencias (1961–2024)

    - Variabilidad vs. Tendencia: El test de Mann–Kendall no mostró tendencias con significancia estadística global, lo que indica que predomina la variabilidad natural.
    
    - Cambio entre Subperíodos: Al comparar 1961–1990 frente a 1991–2020, se detectó un incremento en la intensidad y frecuencia (RX1day, RX5day, R10mm, R20mm) y una disminución en periodos secos (CDD).
    
    - Diagnóstico: Los datos sugieren una señal incipiente hacia un régimen de lluvias más irregular y concentrado, especialmente en las estaciones de verano e invierno.
    
2. Modelado Estadístico (Regresión Múltiple)

    - Alta Capacidad Explicativa: Se lograron modelos robustos para la cantidad total e intensidad:
        - PRCPTOT: $R^2 = 0.97$
        - RX1day: $R^2 = 0.82$
    
    - Interdependencia: Los resultados demuestran que la intensidad de los eventos extremos puede explicarse casi en su totalidad por la combinación lineal de variables de frecuencia.
    
    - Complejidad en Persistencia: El bajo ajuste del índice CWD ($R^2 = 0.16$) revela que la duración de los periodos húmedos responde a dinámicas no lineales o factores meteorológicos más complejos (sinópticos) que no dependen puramente de la intensidad.

**Autores**: Franco Leandro Kumichel & Juan Francisco Volpe Giangiordano
**Institución**: Facultad de Informática - Universidad Nacional de La Plata (UNLP)