# 🏆 UAB THE HACK! 2025 Winner · Analizador Geoespacial WiFi

<p align="center">
  <img src="https://img.shields.io/badge/Winner-UAB%20THE%20HACK!%202025-FFD700?style=for-the-badge" alt="Winner UAB THE HACK 2025" />
  <img src="https://img.shields.io/badge/Challenge-WiFi%20Analytics-38BDF8?style=for-the-badge" alt="WiFi Challenge" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Folium-Geospatial%20Maps-2E7D32?style=for-the-badge" alt="Folium" />
</p>

Proyecto ganador del **reto WiFi de UAB THE HACK! 2025**, desarrollado para transformar datos anonimizados de la red WiFi del campus en información visual, geoespacial e interactiva.

La solución combina **procesamiento y agregación de datos**, conversión de coordenadas geográficas, generación de mapas temporales, análisis de puntos de acceso, un dashboard web y una integración con **AINA** para realizar consultas sobre el contexto y los datos disponibles.

---

## 🚀 El proyecto

El reto consistía en trabajar con grandes volúmenes de datos anonimizados de la red WiFi de la Universitat Autònoma de Barcelona y convertirlos en información que pudiera interpretarse visualmente.

A partir de información sobre:

* puntos de acceso;
* clientes conectados;
* métricas de salud de conexión;
* intensidad de señal;
* carga por punto de acceso;
* posición geográfica;
* evolución temporal;

el sistema procesa y agrega los datos para generar **mapas interactivos con evolución temporal**.

El resultado permite observar cómo cambia el comportamiento de la red según la zona y la hora, utilizando distintas métricas para representar su estado.

El proyecto incorpora además un dashboard web con un chatbot conectado a **AINA**, utilizado para realizar consultas a partir del contexto preparado para el reto.

---

## 🏆 Resultado

El proyecto fue desarrollado en equipo durante **UAB THE HACK! 2025** y resultó **ganador del reto WiFi**.

La solución se centró en convertir información de red difícil de interpretar directamente en mapas, métricas y visualizaciones que permitieran explorar su comportamiento de una forma más accesible.

---

## 🧠 Funcionalidades principales

* Visualización geoespacial de datos WiFi del campus.
* Conversión de coordenadas UTM a latitud y longitud.
* Mapas dinámicos con evolución temporal por hora.
* Análisis de salud media de conexión.
* Análisis de intensidad media de señal.
* Visualización de clientes conectados por punto de acceso.
* Backend mediante FastAPI.
* Frontend ligero en HTML, CSS y JavaScript.
* Integración con AINA mediante API.
* Procesamiento y agregación de datos con Pandas.
* Generación reproducible de mapas a partir del dataset original.
* Scripts de ejecución para distintos entornos.

---

## 🏗️ Arquitectura general

```text
Dataset WiFi anonimizado
        │
        ▼
Procesamiento y filtrado
      Pandas
        │
        ▼
Conversión geoespacial
 PyProj · EPSG:25831
           ↓
       EPSG:4326
        │
        ▼
Agregación temporal
por AP · día · hora
        │
        ▼
Generación de mapas
Folium · TimestampedGeoJson
        │
        ├───────────────┐
        ▼               ▼
   Dashboard         Backend
HTML/CSS/JS          FastAPI
                        │
                        ▼
                      AINA
```

---

## 🛠️ Stack utilizado

| Área                   | Tecnologías                                            |
| ---------------------- | ------------------------------------------------------ |
| Backend                | Python · FastAPI · Uvicorn                             |
| Frontend               | HTML · CSS · JavaScript                                |
| Visualización          | Folium · TimestampedGeoJson · OpenStreetMap            |
| Procesamiento de datos | Pandas · NumPy · JSON                                  |
| Geoespacial            | PyProj · EPSG:25831 · EPSG:4326                        |
| IA                     | AINA API · contexto personalizado                      |
| Herramientas           | Git · Bash · PowerShell · entornos virtuales de Python |

---

## 🗺️ Mapas generados

El script principal `main.py` procesa los datos de puntos de acceso y clientes conectados y genera tres mapas dinámicos e interactivos en HTML.

| Archivo                       | Métrica principal         | Visualización                                       |
| ----------------------------- | ------------------------- | --------------------------------------------------- |
| `mapa_health_dinamico.html`   | Salud media de conexión   | Círculos con gradiente según la calidad de conexión |
| `mapa_signal_dinamico.html`   | Intensidad media de señal | Círculos coloreados según la señal media en dBm     |
| `mapa_clientes_dinamico.html` | Número de clientes por AP | Radio dinámico según la carga del punto de acceso   |

Los mapas incorporan un **slider temporal** y controles de reproducción para recorrer las distintas horas disponibles en el dataset.

---

## ⚙️ Procesamiento de los datos

### 1. Carga

`main.py` trabaja principalmente con dos archivos procesados:

```text
rookie_filtered_aps.json
rookie_filtered_clients.json
```

`rookie_filtered_aps.json` contiene información sobre los puntos de acceso y sus coordenadas.

`rookie_filtered_clients.json` contiene información relacionada con clientes conectados, timestamps, señal, salud de conexión y otras métricas utilizadas durante el análisis.

### 2. Conversión geoespacial

Las coordenadas originales se convierten desde:

```text
EPSG:25831
```

a:

```text
EPSG:4326
```

para poder representarlas mediante latitud y longitud en mapas web.

### 3. Agregación temporal

Los datos se agrupan principalmente por:

```text
punto de acceso
día
hora
```

A partir de ellos se calculan métricas como:

```text
avg_health
avg_signal_db
num_clients_metricos
```

### 4. Generación de mapas

La visualización utiliza:

```text
Folium
TimestampedGeoJson
```

Esto permite representar la evolución de las métricas a lo largo del tiempo y reproducirlas de forma interactiva.

### 5. Salida

Se generan tres archivos HTML:

```text
mapa_health_dinamico.html
mapa_signal_dinamico.html
mapa_clientes_dinamico.html
```

Estos archivos pueden abrirse directamente en un navegador o integrarse en el frontend del proyecto.

---

## 🧩 Aplicaciones incluidas

### Backend

El backend está desarrollado con **FastAPI** y permite:

* comprobar el estado del servidor;
* recibir preguntas desde el frontend;
* construir el contexto utilizado por la IA;
* enviar consultas a AINA;
* devolver las respuestas al dashboard.

Endpoints principales:

| Método | Ruta        | Descripción                                                 |
| ------ | ----------- | ----------------------------------------------------------- |
| `GET`  | `/health`   | Comprueba que el backend está activo                        |
| `POST` | `/api/chat` | Recibe un mensaje y devuelve la respuesta del sistema de IA |

El endpoint de chat recibe datos con la forma:

```json
{
  "message": "<texto>"
}
```

La variable `FRONTEND_ORIGINS` permite configurar los orígenes autorizados mediante CORS.

---

### Frontend

El frontend utiliza **HTML, CSS y JavaScript**.

Se encarga de:

* mostrar el dashboard;
* integrar los mapas generados;
* enviar consultas al backend;
* visualizar las respuestas del chatbot conectado a AINA.

---

## 📁 Estructura del repositorio

```text
.
├── apps/
│   ├── backend/              # FastAPI, cliente de AINA y endpoints
│   └── frontend/             # Dashboard, mapas y llamadas al backend
│
├── data/
│   ├── context/
│   │   └── ai/               # Prompt base y contexto utilizado por AINA
│   │
│   ├── processed/
│   │   └── rookie/           # Datos procesados para generar los mapas
│   │
│   └── raw/
│       ├── anonymized_data/  # Ubicación esperada del dataset original
│       └── snapshots/        # Muestras pequeñas para pruebas
│
├── docs/
│   └── hackathon-kit/        # Materiales y utilidades del reto
│
├── packages/
│   └── geolocation/          # Utilidades de visualización geoespacial
│
├── scripts/                  # Scripts de ejecución
├── main.py                   # Generador principal de mapas
└── README.md
```

---

## 📦 Dataset y reproducibilidad

El **dataset original utilizado durante UAB THE HACK! 2025 no se distribuye mediante este repositorio**.

Los datos pertenecen al contexto del reto y existen restricciones de distribución, por lo que para reproducir el procesamiento completo es necesario disponer previamente de acceso autorizado al dataset original.

El repositorio conserva el código, estructura y scripts utilizados para procesar esos datos.

Además, algunos de los archivos procesados y generados pueden alcanzar tamaños muy elevados, por lo que tampoco se mantienen versionados en Git.

### Archivos no incluidos

| Ubicación                | Archivos                                                    | Cómo obtenerlos                          |
| ------------------------ | ----------------------------------------------------------- | ---------------------------------------- |
| `data/processed/rookie/` | `rookie_filtered_aps.json` · `rookie_filtered_clients.json` | Generarlos a partir del dataset original |
| `apps/frontend/maps/`    | Mapas HTML dinámicos                                        | Ejecutar `python main.py`                |
| Otras salidas generadas  | JSON procesados y mapas                                     | Regenerarlos localmente                  |

Los JSON procesados pueden alcanzar varios GB y algunos mapas HTML pueden ocupar cientos de MB.

Por este motivo, el objetivo del repositorio es conservar **el código y el flujo de procesamiento**, no redistribuir los datos originales ni todos los artefactos generados.

---

## ✅ Requisitos

* Python 3.10 o superior.
* `pip`.
* Navegador moderno.
* Conexión a Internet para cargar los tiles de OpenStreetMap.
* PowerShell 7+ en Windows o bash/zsh en macOS/Linux.
* Acceso autorizado al dataset original para regenerar todos los datos.
* `AINA_API_KEY` si se desea utilizar la integración con AINA mediante un token propio.

Dependencias principales:

```bash
pip install folium pandas pyproj branca
pip install numpy pytz python-dateutil tzdata requests
```

---

## ⚡ Instalación

Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd uab-the-hack-2025-wifi-analytics
```

Crea un entorno virtual:

```bash
python -m venv .venv
```

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.\.venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r apps/backend/requirements.txt
```

---

## ▶️ Ejecución

### Mediante scripts

Linux / macOS:

```bash
./scripts/run_backend.sh
./scripts/run_frontend.sh
```

Windows:

```powershell
pwsh scripts/run_backend.ps1
pwsh scripts/run_frontend.ps1
```

---

### Ejecución manual

Inicia el backend:

```bash
cd apps/backend
uvicorn main:app --reload
```

En otra terminal, inicia el frontend:

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

## 🗺️ Regenerar los mapas

Para generar los mapas es necesario disponer previamente de los datos procesados correspondientes.

Con el entorno preparado:

```bash
python main.py
```

Se generarán:

```text
apps/frontend/maps/mapa_health_dinamico.html
apps/frontend/maps/mapa_signal_dinamico.html
apps/frontend/maps/mapa_clientes_dinamico.html
```

Estos archivos pueden alcanzar cientos de MB y no se versionan en el repositorio.

---

## 🧪 Generar los JSON procesados

Para generar:

```text
rookie_filtered_aps.json
rookie_filtered_clients.json
```

es necesario disponer de acceso autorizado al dataset original utilizado durante el reto.

Los datos deben situarse en:

```text
data/raw/anonymized_data/aps
data/raw/anonymized_data/clients
```

Después puede ejecutarse:

```bash
python docs/hackathon-kit/scripts/create_filtered_json.py \
  --aps-dir data/raw/anonymized_data/aps \
  --clients-dir data/raw/anonymized_data/clients \
  --aps-output data/processed/rookie/rookie_filtered_aps.json \
  --clients-output data/processed/rookie/rookie_filtered_clients.json \
  --skip-combined
```

Los archivos resultantes pueden alcanzar varios GB, por lo que no se recomienda versionarlos mediante Git.

---

## 🤖 Integración con AINA

El proyecto incluye una integración con **AINA** mediante el backend.

El contexto utilizado por el sistema puede configurarse desde:

```text
data/context/ai/
```

Para utilizar un token propio debe definirse:

```bash
export AINA_API_KEY="tu_token"
```

En Windows PowerShell:

```powershell
$env:AINA_API_KEY="tu_token"
```

Después debe reiniciarse el backend para que recoja la variable de entorno.

> La clave de API nunca debe añadirse directamente al repositorio.

---

## 🧯 Problemas habituales

| Problema                  | Posible solución                                                           |
| ------------------------- | -------------------------------------------------------------------------- |
| El mapa aparece sin fondo | Comprueba la conexión a Internet; OpenStreetMap necesita cargar los tiles  |
| Faltan datos              | El dataset original y los archivos procesados completos no están incluidos |
| Los mapas no existen      | Regenera los archivos ejecutando `python main.py`                          |
| Error de CORS             | Revisa la configuración de `FRONTEND_ORIGINS`                              |
| Faltan dependencias       | Instálalas dentro del entorno virtual                                      |
| AINA no responde          | Revisa `AINA_API_KEY` y reinicia el backend                                |

---

## 👥 Equipo

Proyecto desarrollado **en equipo** durante **UAB THE HACK! 2025**.

El repositorio recoge el trabajo realizado para el reto WiFi, incluyendo procesamiento de datos, visualización geoespacial, backend, frontend e integración con AINA.

---

## 📌 Limitaciones

Este repositorio **no contiene el dataset original completo utilizado durante el hackathon**.

Por tanto, una clonación limpia del repositorio permite consultar el código y la arquitectura del proyecto, pero determinadas funcionalidades relacionadas con el procesamiento y la generación completa de mapas requieren disponer previamente de los datos originales.

Asimismo, algunos archivos procesados y visualizaciones generadas se mantienen fuera de Git debido a su tamaño.

---

## 🔐 Datos y credenciales

* El dataset original no se redistribuye mediante este repositorio.
* No deben publicarse claves de AINA ni otras credenciales.
* Los archivos generados de gran tamaño deben mantenerse fuera de Git.
* El repositorio conserva principalmente el código, la estructura y la documentación necesarios para comprender y reproducir el flujo cuando se dispone de los datos correspondientes.

---

## 🏁 UAB THE HACK! 2025

**Ganador del reto WiFi de UAB THE HACK! 2025.**

Proyecto desarrollado para explorar cómo el procesamiento de datos y la visualización geoespacial pueden facilitar la interpretación de grandes volúmenes de información procedentes de una infraestructura WiFi real.
