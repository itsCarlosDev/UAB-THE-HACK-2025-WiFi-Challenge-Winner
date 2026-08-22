# Generación de mapas

El proyecto incluye un generador de mapas geoespaciales desarrollado en Python.

La versión pública utiliza exclusivamente un pequeño conjunto de datos sintéticos incluido en:

```text
data/demo/
├── rookie_filtered_aps.json
└── rookie_filtered_clients.json
```

El dataset original utilizado durante UAB THE HACK! 2025 no se distribuye mediante este repositorio.

## Flujo

```text
data/demo/
    │
    ▼
Pandas
    │
    ├── agregación por AP y hora
    │
    ▼
PyProj
EPSG:25831 → EPSG:4326
    │
    ▼
Folium + TimestampedGeoJson
    │
    ▼
apps/frontend/maps/
```

## Script

El generador se encuentra en:

```text
scripts/generate_maps.py
```

Desde la raíz del repositorio:

```bash
python scripts/generate_maps.py
```

## Archivos generados

El script crea:

```text
apps/frontend/maps/mapa_health_dinamico.html
apps/frontend/maps/mapa_signal_dinamico.html
apps/frontend/maps/mapa_clientes_dinamico.html
```

Los HTML generados están excluidos mediante `.gitignore`, por lo que se regeneran localmente después de clonar el repositorio.

## Datos de demostración

La demo pública contiene:

- 3 puntos de acceso ficticios: `AP-DEMO-01`, `AP-DEMO-02` y `AP-DEMO-03`;
- 15 observaciones sintéticas;
- 4 franjas horarias: 09:00, 12:00, 15:00 y 18:00.

Los identificadores, métricas y ubicaciones son de demostración y no representan la infraestructura real de la UAB.

## Qué representa cada mapa

### Health

Muestra la media de la métrica `health` para cada AP y franja temporal.

### Señal

Muestra la intensidad media de señal (`signal_db`) en dBm para cada AP y franja temporal.

### Actividad

Representa el número de observaciones asociadas a cada AP. El tamaño de los elementos cambia según la carga representada.

## Limitaciones

La demo es deliberadamente pequeña y sirve para comprobar el pipeline técnico.

No permite reproducir las conclusiones obtenidas durante el hackathon ni debe utilizarse para inferir el estado actual de la red WiFi de la Universitat Autònoma de Barcelona.
