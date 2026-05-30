# 🏆 UAB THE HACK! 2025 Winner · Analizador Geoespacial WiFi

<p align="center">
  <img src="https://img.shields.io/badge/Winner-UAB%20THE%20HACK!%202025-FFD700?style=for-the-badge" alt="Winner UAB THE HACK 2025" />
  <img src="https://img.shields.io/badge/Challenge-WiFi%20Analytics-38BDF8?style=for-the-badge" alt="WiFi Challenge" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Folium-Geospatial%20Maps-2E7D32?style=for-the-badge" alt="Folium" />
</p>

Proyecto ganador del **reto WiFi de UAB THE HACK! 2025**, desarrollado para analizar datos anonimizados de la red WiFi del campus y convertirlos en información visual, geoespacial e interactiva.

El proyecto combina procesamiento de datos, generación de mapas dinámicos, análisis de puntos de acceso, visualización temporal y un dashboard web con integración de IA mediante AINA.

---

## 🚀 Resumen del proyecto

El objetivo del proyecto era transformar grandes volúmenes de datos WiFi anonimizados en una herramienta útil para entender el comportamiento de la red del campus.

A partir de datos de **puntos de acceso**, **clientes conectados**, métricas de salud, intensidad de señal y carga por zona, el sistema genera mapas interactivos que permiten visualizar la evolución temporal de la red.

Además, el dashboard incluye un chatbot conectado a AINA para facilitar preguntas sobre los datos, el contexto del reto y posibles decisiones técnicas.

---

## 🧠 Qué aporta

* Visualización geoespacial de datos WiFi del campus.
* Conversión de coordenadas UTM a latitud/longitud para mapas web.
* Mapas dinámicos con evolución temporal por hora.
* Análisis de salud de conexión, señal y número de clientes por punto de acceso.
* Backend con FastAPI para servir endpoints propios y conectar con AINA.
* Frontend ligero en HTML, CSS y JavaScript.
* Organización del dataset, scripts y documentación oficial del reto.
* Flujo reproducible para regenerar mapas y datos filtrados localmente.

---

## 🛠️ Stack utilizado

| Área          | Tecnologías                                      |
| ------------- | ------------------------------------------------ |
| Backend       | Python · FastAPI · Uvicorn                       |
| Frontend      | HTML · CSS · JavaScript                          |
| Visualización | Folium · TimestampedGeoJson · OpenStreetMap      |
| Datos         | Pandas · JSON · datasets anonimizados            |
| Geoespacial   | PyProj · EPSG:25831 · EPSG:4326                  |
| IA            | AINA API · contexto personalizado                |
| Herramientas  | Bash · PowerShell · Git · entorno virtual Python |

---

## 📁 Estructura del repositorio

```txt
.
├── apps/
│   ├── backend/             # FastAPI, cliente de AINA y endpoints propios
│   └── frontend/            # Web estática, mapas y llamadas al backend
├── data/
│   ├── context/ai/          # Prompt base y archivos de contexto para el LLM
│   ├── processed/rookie/    # Datos agregados listos para mapas
│   └── raw/
│       ├── anonymized_data/ # Dataset oficial anonimizado de la UAB
│       └── snapshots/       # Muestras pequeñas para pruebas rápidas
├── docs/hackathon-kit/      # Manuales, logos y materiales oficiales del reto
├── packages/geolocation/    # Utilidades y ejemplos de visualización
├── scripts/                 # Scripts de lanzamiento para bash y PowerShell
├── main.py                  # Generación principal de mapas dinámicos
└── .venv/                   # Entorno virtual local opcional
```

---

## 🗺️ Mapas generados

El script principal `main.py` procesa los datos de puntos de acceso y clientes conectados para generar tres mapas dinámicos e interactivos en HTML.

| Archivo                       | Métrica principal         | Visualización                                        |
| ----------------------------- | ------------------------- | ---------------------------------------------------- |
| `mapa_health_dinamico.html`   | Salud media de conexión   | Círculos con gradiente de rojo a verde según calidad |
| `mapa_signal_dinamico.html`   | Intensidad media de señal | Círculos coloreados según señal media en dBm         |
| `mapa_clientes_dinamico.html` | Número de clientes por AP | Radio dinámico según carga por punto de acceso       |

Todos los mapas incluyen un slider temporal y botón de reproducción para recorrer las horas del dataset.

---

## ⚙️ Cómo funciona `main.py`

1. **Carga de datos**

   * `rookie_filtered_aps.json`: puntos de acceso con nombre y coordenadas UTM.
   * `rookie_filtered_clients.json`: clientes conectados, timestamps, salud, señal y métricas asociadas.

2. **Conversión geoespacial**

   * Convierte coordenadas UTM `EPSG:25831` a latitud/longitud `EPSG:4326`.

3. **Agregación temporal**

   * Agrupa por punto de acceso, día y hora.
   * Calcula métricas como `avg_health`, `avg_signal_db` y `num_clients_metricos`.

4. **Generación de mapas**

   * Usa Folium y `TimestampedGeoJson`.
   * Genera visualizaciones animadas con duración horaria.
   * Centra la escena en la zona de Veterinaria del campus.

5. **Salida**

   * Genera tres archivos HTML interactivos listos para abrir o integrar en el frontend.

---

## 🧩 Aplicaciones incluidas

### Backend

Backend desarrollado con FastAPI para:

* Comprobar el estado del servidor.
* Recibir preguntas desde el frontend.
* Construir contexto para la IA.
* Enviar consultas a AINA.
* Devolver respuestas al dashboard.

### Frontend

Frontend ligero en HTML, CSS y JavaScript para:

* Mostrar el dashboard.
* Integrar los mapas generados.
* Enviar preguntas al backend.
* Visualizar respuestas del chatbot AINA.

---

## 📦 Archivos pesados fuera del repositorio

GitHub rechaza archivos superiores a 100 MB. Por eso, los datasets completos y los HTML generados no se versionan en el repositorio.

| Carpeta                    | Archivos locales                                                                        | Cómo recuperarlos                                                   |
| -------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data/processed/rookie/`   | `rookie_filtered_aps.json`, `rookie_filtered_clients.json`                              | Generarlos con `docs/hackathon-kit/scripts/create_filtered_json.py` |
| `docs/hackathon-kit/data/` | Copia de `rookie_filtered_*.json`                                                       | Descargar desde el enlace incluido en `onedrive.txt`                |
| `frontend/`                | JSON filtrados y mapas HTML legacy                                                      | Generar localmente con `python frontend/main.py`                    |
| `apps/frontend/maps/`      | `mapa_health_dinamico.html`, `mapa_signal_dinamico.html`, `mapa_clientes_dinamico.html` | Regenerar ejecutando `python main.py`                               |

Los archivos generados pueden pesar cientos de MB, por lo que deben mantenerse en local o compartirse mediante almacenamiento externo.

---

## ✅ Requisitos

* Python 3.10 o superior.
* `pip`.
* PowerShell 7+ en Windows o bash/zsh en macOS/Linux.
* Navegador moderno.
* Conexión a internet para cargar tiles de OpenStreetMap.
* Variable `AINA_API_KEY` si se quiere usar un token propio.

Dependencias principales:

```bash
pip install folium pandas pyproj branca
pip install numpy pytz python-dateutil tzdata requests
```

---

## ⚡ Instalación rápida

```bash
git clone <este_repo>
cd uab-the-hack-2025-wifi-analytics

python -m venv .venv
source .venv/bin/activate

pip install -r apps/backend/requirements.txt
```

En Windows:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\activate
pip install -r apps/backend/requirements.txt
```

---

## ▶️ Ejecución

### Usando scripts

```bash
./scripts/run_backend.sh
./scripts/run_frontend.sh
```

En PowerShell:

```powershell
pwsh scripts/run_backend.ps1
pwsh scripts/run_frontend.ps1
```

### Modo manual

```bash
cd apps/backend
uvicorn main:app --reload
```

En otra terminal:

```bash
cd apps/frontend
python -m http.server 8001
```

Después abre:

```txt
http://127.0.0.1:8001
```

El frontend llama al backend en:

```txt
http://127.0.0.1:8000/api/chat
```

---

## 🗺️ Regenerar mapas localmente

Los mapas HTML pueden pesar alrededor de 250 MB cada uno, por lo que no se suben a GitHub.

Para regenerarlos:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r apps/backend/requirements.txt
python main.py
```

Los archivos se generarán en:

```txt
apps/frontend/maps/
```

No los subas al repositorio. Mantenlos en local o compártelos mediante almacenamiento externo si hace falta.

---

## 🧪 Generar los JSON filtrados

Los archivos `rookie_filtered_aps.json` y `rookie_filtered_clients.json` resumen el dataset bruto y pueden pesar entre 1 GB y 3 GB.

Para generarlos:

1. Descarga el dataset anonimizado oficial.
2. Colócalo en:

```txt
data/raw/anonymized_data/aps
data/raw/anonymized_data/clients
```

3. Ejecuta:

```bash
python docs/hackathon-kit/scripts/create_filtered_json.py \
  --aps-dir data/raw/anonymized_data/aps \
  --clients-dir data/raw/anonymized_data/clients \
  --aps-output data/processed/rookie/rookie_filtered_aps.json \
  --clients-output data/processed/rookie/rookie_filtered_clients.json \
  --skip-combined
```

En PowerShell puedes usar `^` en lugar de `\`, o ejecutarlo todo en una sola línea.

---

## 🤖 Uso del chatbot AINA

1. Ajusta el prompt base en:

```txt
data/context/ai/el_teu_arxiu.txt
```

2. Añade archivos de contexto adicionales en la misma carpeta si necesitas que AINA tenga más información.

3. Define la variable de entorno:

```bash
export AINA_API_KEY="tu_token"
```

En Windows PowerShell:

```powershell
$env:AINA_API_KEY="tu_token"
```

4. Reinicia el backend para que recoja la variable.

5. Lanza preguntas desde el frontend.

---

## 🔌 API del backend

| Método | Ruta        | Descripción                                                        |
| ------ | ----------- | ------------------------------------------------------------------ |
| GET    | `/health`   | Comprueba que el backend está activo                               |
| POST   | `/api/chat` | Recibe `{ "message": "<texto>" }` y devuelve la respuesta de la IA |

La variable `FRONTEND_ORIGINS` permite ampliar los orígenes autorizados para CORS.

---

## 🧯 Problemas habituales

| Problema                   | Solución                                                          |
| -------------------------- | ----------------------------------------------------------------- |
| Mapa sin fondo             | Folium necesita internet para cargar los tiles de OpenStreetMap   |
| Archivos demasiado grandes | Usa snapshots o genera los archivos localmente sin subirlos a Git |
| Error de CORS              | Ajusta la variable `FRONTEND_ORIGINS`                             |
| Faltan dependencias        | Instala las librerías dentro del entorno virtual                  |
| No responde AINA           | Revisa `AINA_API_KEY` y reinicia el backend                       |

---

## 🏁 Checklist antes de presentar

* [ ] Activar el entorno virtual.
* [ ] Instalar dependencias.
* [ ] Definir `AINA_API_KEY` si se usa token propio.
* [ ] Lanzar backend y frontend.
* [ ] Validar `/health`.
* [ ] Regenerar mapas con `python main.py` si hace falta.
* [ ] Abrir los HTML generados.
* [ ] Probar el chatbot desde el frontend.
* [ ] Revisar que el dashboard y los mapas estén listos para la demo.

---

## 🏆 Resultado

Este proyecto fue desarrollado durante **UAB THE HACK! 2025** y resultó ganador del **reto WiFi**.

El trabajo se centró en convertir datos anonimizados de red en mapas, métricas y visualizaciones útiles para entender mejor el comportamiento de conexión dentro del campus.

---

## 👥 Equipo

Proyecto desarrollado en equipo durante UAB THE HACK! 2025.

---

## 📌 Nota

Los datos originales pertenecen al contexto del reto y no se incluyen completamente en el repositorio por tamaño y restricciones de distribución.

Este repositorio mantiene la estructura, scripts y documentación necesarios para reproducir el flujo de trabajo de forma local.
