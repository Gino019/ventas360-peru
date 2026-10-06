# Ventas360 Perú — dashboard con Streamlit

Dashboard académico de ventas con Python, Streamlit, Pandas y Plotly. Incluye 1.200 líneas de venta **sintéticas**, filtros por ciudad, categoría y fechas, cuatro indicadores, cuatro gráficos, carga y exportación de CSV.

## Contexto del proyecto

**Ventas360 Perú** es un proyecto académico de visualización de datos que demuestra el proceso completo de construcción de un dashboard: preparar datos, calcular indicadores, crear gráficos interactivos, versionar el código y publicar la aplicación en la nube mediante automatización.

La actividad solicita que cada integrante publique un artículo en Medium, Dev.to o Hashnode, incluya un repositorio público y una aplicación alojada en un proveedor cloud o SaaS, y produzca un video público de construcción y demostración de máximo cinco minutos. Este repositorio proporciona la aplicación, las pruebas, el flujo de integración continua y los materiales base para documentar ese proceso.

### Problema que aborda

Una tabla de ventas por sí sola dificulta comparar periodos, ciudades y productos. El dashboard convierte los registros en indicadores y visualizaciones para responder: ¿cuánto se vendió?, ¿qué ciudad concentra las ventas?, ¿cómo evolucionan en el tiempo? y ¿qué productos generan mayor utilidad bruta?

### Objetivo general

Desarrollar y publicar un dashboard interactivo y reproducible para explorar ventas mediante Python y herramientas de visualización, incorporando control de versiones y automatización.

### Objetivos específicos

- Validar y procesar un archivo CSV con Pandas.
- Mostrar ventas, utilidad bruta, unidades y margen bruto.
- Filtrar por ciudad, categoría y fechas y exportar los datos seleccionados.
- Automatizar pruebas con GitHub Actions y actualizar la aplicación desde GitHub con Streamlit Community Cloud.
- Explicar la construcción mediante un artículo y un video de hasta cinco minutos.

### Alcance y datos

La muestra contiene 1.200 líneas de venta sintéticas del primer semestre de 2026 para Tacna, Arequipa, Lima y Cusco, con categorías de Tecnología, Hogar y Belleza. No representa a una empresa real y no permite extraer conclusiones sobre el mercado peruano. La app admite CSV propios con el mismo esquema; no incluye autenticación, base de datos persistente, gestión de inventario ni contabilidad completa.

### Tecnologías

| Herramienta | Función |
| --- | --- |
| Python | Lenguaje de implementación |
| Streamlit | Interfaz web y controles interactivos |
| Pandas y NumPy | Validación, transformación y cálculos |
| Plotly | Gráficos interactivos |
| Pytest y AppTest | Pruebas de lógica e interfaz |
| GitHub Actions | Integración continua: ejecución de pruebas |
| Streamlit Community Cloud | Alojamiento previsto y actualización automática desde GitHub |

### Entregables y enlaces

- Repositorio: https://github.com/Gino019/ventas360-peru
- App pública: pendiente de despliegue y verificación.
- Artículo Medium: pendiente de publicación; borrador en [docs/articulo_medium.md](docs/articulo_medium.md).
- Video público: pendiente de grabación; guion en [docs/guion_video.md](docs/guion_video.md).

## Ejecutar (Python 3.11 o superior)

```bash
git clone https://github.com/Gino019/ventas360-peru.git
cd ventas360-peru
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
