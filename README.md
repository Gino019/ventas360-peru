# Ventas Perú — dashboard con Streamlit

Dashboard académico de ventas con Python, Streamlit, Pandas y Plotly. Incluye 1.200 líneas de venta **sintéticas**, filtros por ciudad, categoría y fechas, cuatro indicadores, cuatro gráficos, carga y exportación de CSV.

## Ejecutar (Python 3.11 o superior)

```bash
python -m venv .venv
```

Windows PowerShell: `.venv\Scripts\Activate.ps1`
Linux/macOS: `source .venv/bin/activate`

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Abrir http://localhost:8501. En Windows también se puede ejecutar `iniciar.bat` (requiere Python instalado).

## Probar

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Publicación y automatización

1. Subir este proyecto a un repositorio público de GitHub, en la raíz de la rama `main`.
2. Entrar en https://share.streamlit.io/ con acceso al repositorio.
3. Crear una app, seleccionar repositorio, rama `main` y archivo `app.py`.
4. En ajustes avanzados, seleccionar Python 3.11 y desplegar. Configurar acceso público.
5. Abrir el enlace público en una ventana privada para comprobarlo.
6. Un nuevo push a `main` actualiza la app automáticamente a través de Community Cloud.

GitHub Actions ejecuta pruebas en pushes a main y pull requests. **El workflow es CI; Community Cloud proporciona CD.** La configuración inicial de alojamiento se hace una vez. No existe un bloqueo entre CI y CD por defecto: para exigir pruebas exitosas antes de publicar, configurar protección de `main`, requerir el check `tests` y trabajar mediante pull requests.

## CSV

UTF-8, separado por comas. Columnas: `fecha,ciudad,categoria,producto,cantidad,precio_unitario,costo_unitario`. Fechas AAAA-MM-DD; cantidad entera positiva; precios y costos no negativos, punto decimal. Máximo 10 MB y 100.000 filas. Ver `data/ventas_demo.csv`.

Cada fila es una línea de venta, no necesariamente un pedido completo. Ventas = cantidad × precio; utilidad bruta = ventas − costo de productos; margen = utilidad / ventas × 100. No se calcula utilidad neta. Las pérdidas brutas son válidas si el costo supera al precio. El CSV cargado se procesa en la sesión y no se escribe al repositorio.

## Estructura

- `app.py`: interfaz y gráficos.
- `analytics.py`: validaciones, indicadores y exportación.
- `data/ventas_demo.csv`: muestra sintética.
- `tests/test_app.py`: pruebas de cálculos, errores y filtros.
- `.github/workflows/ci.yml`: pruebas automáticas.
- `docs/`: artículo, guion y checklist de entrega.

## Estado

App preparada y pruebas locales incluidas. Completar despliegue y enlaces reales antes de entregar. No se incluyen claves ni cuentas cloud.
