# 🏆 UAB THE HACK! 2025 Winner · Analizador Geoespacial WiFi

<p align="center">
  <img src="https://img.shields.io/badge/Winner-UAB%20THE%20HACK!%202025-FFD700?style=for-the-badge" alt="Winner UAB THE HACK 2025" />
  <img src="https://img.shields.io/badge/Challenge-WiFi%20Analytics-38BDF8?style=for-the-badge" alt="WiFi Challenge" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Folium-Geospatial%20Maps-2E7D32?style=for-the-badge" alt="Folium" />
</p>

Proyecto ganador del **reto WiFi de UAB THE HACK! 2025**, desarrollado en equipo para transformar datos anonimizados de una infraestructura WiFi de campus en información visual, geoespacial e interactiva.

La solución combina procesamiento y agregación de datos, conversión de coordenadas, generación de mapas temporales, análisis de puntos de acceso, un dashboard web y una integración con **AINA**.

> El dataset original utilizado durante el hackathon no se distribuye mediante este repositorio.
>
> Para mantener el proyecto reproducible sin redistribuir esos datos, se incluye una pequeña **demo con datos sintéticos**.

---

## 🚀 El proyecto

El reto consistía en trabajar con grandes volúmenes de información de la red WiFi de la Universitat Autònoma de Barcelona y convertir esos datos en visualizaciones que permitieran interpretar mejor su comportamiento.

El sistema desarrollado trabaja con información relacionada con:

- puntos de acceso;
- clientes asociados;
- métricas de salud de conexión;
- intensidad de señal;
- carga por punto de acceso;
- posición geográfica;
- evolución temporal.

Los datos se procesan y agregan para generar mapas interactivos que permiten recorrer distintas franjas temporales.

También se desarrolló un dashboard web y una integración con **AINA** para realizar consultas sobre un contexto previamente preparado.

---

## 🏆 Resultado

El proyecto fue desarrollado en equipo durante **UAB THE HACK! 2025** y resultó **ganador del reto WiFi**.

La solución buscaba convertir grandes volúmenes de información difícil de interpretar directamente en métricas y visualizaciones geoespaciales más accesibles.

---

## 🧠 Funcionalidades principales

- Procesamiento y agregación de datos mediante Pandas.
- Conversión de coordenadas UTM a latitud y longitud.
- Mapas dinámicos con evolución temporal.
- Análisis de la métrica `health`.
- Análisis de intensidad de señal en dBm.
- Visualización de carga por punto de acceso.
- Análisis temporal de actividad.
- Backend desarrollado con FastAPI.
- Frontend ligero en HTML, CSS y JavaScript.
- Integración opcional con AINA mediante API.
- Demo reproducible mediante datos sintéticos.
- Scripts de ejecución para Windows y Linux/macOS.

---

## 🏗️ Arquitectura

```text
            data/demo/
        datos sintéticos
               │
               ▼
             Pandas
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
análisis temporal   agregación AP/hora
       │                │
       │                ▼
       │             PyProj
       │      EPSG:25831 → EPSG:4326
       │                │
       │                ▼
       │              Folium
       │                │
       │                ▼
       │         mapas dinámicos
       │                │
       └────────┬───────┘
                ▼
             Frontend
         HTML / CSS / JS

                +

             FastAPI
                │
                ▼
              AINA
```

---

## 🛠️ Stack

| Área | Tecnologías |
| --- | --- |
| Backend | Python · FastAPI · Uvicorn |
| Frontend | HTML · CSS · JavaScript |
| Visualización | Folium · TimestampedGeoJson · OpenStreetMap |
| Procesamiento | Pandas · NumPy · JSON |
| Geoespacial | PyProj · EPSG:25831 · EPSG:4326 |
| IA | AINA API |
| Herramientas | Git · Bash · PowerShell · entornos virtuales de Python |

---

## 📁 Estructura del repositorio

```text
.
├── apps/
│   ├── backend/
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   ├── sandboxes/
│   │   └── services/
│   │
│   └── frontend/
│       ├── index.html
│       ├── app.js
│       ├── styles.css
│       └── maps/
│           └── README.md
│
├── data/
│   ├── context/
│   │   └── ai/
│   │       └── el_teu_arxiu.txt
│   │
│   └── demo/
│       ├── rookie_filtered_aps.json
│       └── rookie_filtered_clients.json
│
├── docs/
│   └── map-generation.md
│
├── scripts/
│   ├── generate_maps.py
│   ├── analyze_peak_usage.py
│   ├── run_backend.ps1
│   ├── run_backend.sh
│   ├── run_frontend.ps1
│   └── run_frontend.sh
│
├── .gitignore
└── README.md
```

---

## 🧪 Demo con datos sintéticos

El repositorio incluye un pequeño conjunto de datos sintéticos:

```text
data/demo/rookie_filtered_aps.json
data/demo/rookie_filtered_clients.json
```

La demo actual contiene:

- **3 puntos de acceso ficticios**: `AP-DEMO-01`, `AP-DEMO-02` y `AP-DEMO-03`;
- **15 observaciones sintéticas**;
- diferentes franjas horarias para probar agregación, señal, `health` y carga por AP.

Estos datos **no representan la infraestructura real de la UAB**.

Su objetivo es permitir que una clonación limpia del repositorio pueda ejecutar las partes principales del proyecto sin disponer del dataset original del evento.

---

## 🗺️ Mapas dinámicos

El generador se encuentra en:

```text
scripts/generate_maps.py
```

Procesa:

```text
data/demo/rookie_filtered_aps.json
data/demo/rookie_filtered_clients.json
```

y genera:

```text
apps/frontend/maps/mapa_health_dinamico.html
apps/frontend/maps/mapa_signal_dinamico.html
apps/frontend/maps/mapa_clientes_dinamico.html
```

Los mapas utilizan `TimestampedGeoJson` para representar la evolución temporal de las métricas.

### Health

Representa la media de la métrica `health` por AP y franja temporal.

### Señal

Representa la intensidad media de señal en dBm.

### Clientes

Representa mediante el tamaño de los elementos el número de observaciones asociadas a cada AP.

Los archivos HTML generados se mantienen fuera de Git y pueden regenerarse localmente.

---

## 📊 Análisis temporal

El repositorio también incluye:

```text
scripts/analyze_peak_usage.py
```

Este script analiza el dataset sintético y calcula:

- actividad por hora;
- franjas con mayor número de registros;
- distribución de actividad por AP ficticio.

Para ejecutarlo:

```bash
python scripts/analyze_peak_usage.py
```

Los resultados corresponden exclusivamente a los datos sintéticos de demostración.

---

## ⚙️ Instalación

Clona el repositorio:

```bash
git clone https://github.com/itsCarlosDev/UAB-THE-HACK-2025-WiFi-Challenge-Winner.git
cd UAB-THE-HACK-2025-WiFi-Challenge-Winner
```

Crea un entorno virtual:

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Instala las dependencias:

```bash
python -m pip install -r apps/backend/requirements.txt
```

---

## 🗺️ Generar los mapas

Desde la raíz del repositorio:

```bash
python scripts/generate_maps.py
```

Si termina correctamente se crearán:

```text
apps/frontend/maps/mapa_health_dinamico.html
apps/frontend/maps/mapa_signal_dinamico.html
apps/frontend/maps/mapa_clientes_dinamico.html
```

Estos archivos están incluidos en `.gitignore` y se generan localmente.

---

## ▶️ Ejecutar el proyecto

### Backend

Desde la raíz:

```bash
cd apps/backend
uvicorn main:app --reload
```

El backend queda disponible en:

```text
http://127.0.0.1:8000
```

### Frontend

En otra terminal:

```bash
cd apps/frontend
python -m http.server 8001
```

Después abre:

```text
http://127.0.0.1:8001
```

El frontend utiliza el backend en:

```text
http://127.0.0.1:8000/api/chat
```

---

## 🤖 Integración con AINA

La integración con AINA es opcional.

La clave debe proporcionarse mediante la variable de entorno:

```text
AINA_API_KEY
```

### Windows PowerShell

```powershell
$env:AINA_API_KEY="tu_token"
```

### Linux / macOS

```bash
export AINA_API_KEY="tu_token"
```

La clave no debe almacenarse directamente en el código ni incluirse en Git.

El contexto utilizado por el cliente se encuentra en:

```text
data/context/ai/el_teu_arxiu.txt
```

La versión destinada al repositorio utiliza contexto de demostración y no debe contener información sensible de infraestructura.

---

## 📦 Dataset original

Durante UAB THE HACK! 2025 se trabajó con el dataset proporcionado para el reto.

Ese dataset **no está incluido en este repositorio**.

Tampoco se incluyen en la versión preparada para publicación:

- snapshots originales;
- identificadores reales de infraestructura;
- coordenadas originales de puntos de acceso;
- archivos originales de clientes;
- credenciales utilizadas durante el evento.

El repositorio conserva el código y una demo sintética suficiente para ejecutar y estudiar el flujo principal.

---

## 🔐 Datos y credenciales

Antes de publicar cambios se debe comprobar que el repositorio no incluya:

- datasets originales;
- archivos `.env`;
- claves API;
- identificadores o coordenadas reales de infraestructura;
- artefactos generados innecesarios.

Los archivos locales de configuración y los mapas HTML generados se excluyen mediante `.gitignore`.

---

## 👥 Equipo

Proyecto desarrollado **en equipo** durante **UAB THE HACK! 2025**.

El repositorio recoge trabajo realizado para el reto WiFi en procesamiento de datos, visualización geoespacial, frontend, backend e integración con IA.

---

## 📌 Limitaciones

La demo incluida es deliberadamente pequeña y sintética.

Sirve para demostrar el funcionamiento técnico del pipeline, pero no permite reproducir las conclusiones obtenidas durante el hackathon ni representa el estado real de la infraestructura WiFi de la UAB.

La integración con AINA requiere que cada usuario proporcione su propia clave de API.

---

## 🏁 UAB THE HACK! 2025

**Ganador del reto WiFi de UAB THE HACK! 2025.**

El proyecto exploró cómo el procesamiento de datos, el análisis temporal y la visualización geoespacial pueden ayudar a interpretar grandes volúmenes de información procedentes de una infraestructura WiFi real.
