# Mapas dinámicos generados

Esta carpeta contiene los mapas HTML generados localmente por:

```text
scripts/generate_maps.py
```

El script crea:

```text
mapa_health_dinamico.html
mapa_signal_dinamico.html
mapa_clientes_dinamico.html
```

Para generarlos desde la raíz del repositorio:

```bash
python scripts/generate_maps.py
```

La versión pública utiliza exclusivamente los datos sintéticos incluidos en:

```text
data/demo/
```

Los archivos `.html` generados están excluidos mediante `.gitignore` y no se versionan.

Después de clonar el repositorio deben generarse localmente antes de abrir los mapas desde el dashboard.

Los AP, métricas y ubicaciones de la demo no representan la infraestructura real de la UAB.
