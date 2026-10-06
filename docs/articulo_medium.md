# De un archivo CSV a un dashboard de ventas con Python, Streamlit y despliegue automático

Autor: Eduardo Gino Flores Navarro

> Borrador para Medium. Completar los tres enlaces y agregar capturas propias después de verificar la publicación. Las instrucciones de despliegue describen el procedimiento; no son evidencia de que ya esté ejecutado.

## El objetivo: entender las ventas de forma visual

Una tabla permite almacenar información, pero puede ser difícil reconocer rápidamente qué ciudad genera más ventas o qué productos aportan mayor utilidad. Este proyecto transforma un archivo CSV en un dashboard interactivo: Ventas360 Perú.

La aplicación permite explorar ventas por ciudad, categoría y periodo. Presenta indicadores y gráficos que se actualizan con los filtros, y permite descargar el conjunto seleccionado para continuar el análisis.

Para que cualquier persona pueda reproducir el ejercicio, el repositorio incluye 1.200 registros sintéticos correspondientes al primer semestre de 2026. Se consideran Tacna, Arequipa, Lima y Cusco, y las categorías Tecnología, Hogar y Belleza. Estos datos fueron generados para la demostración y no representan actividad comercial real.

## Herramientas utilizadas

Streamlit construye la interfaz web desde Python. Pandas lee, valida, filtra y agrupa el CSV. Plotly genera gráficos interactivos. GitHub mantiene el código y su historial; GitHub Actions ejecuta las pruebas. Para publicar la aplicación se utiliza Streamlit Community Cloud, conectado al repositorio.

Esta separación permite explicar el recorrido completo: datos, procesamiento, visualización, control de versiones y publicación.

## 1. Organizar el proyecto

La interfaz está en `app.py`, mientras que `analytics.py` concentra las validaciones y los cálculos. La carpeta `data` contiene el CSV de demostración y `tests` contiene las pruebas. Las versiones de las dependencias están declaradas en `requirements.txt`.

Para ejecutarlo localmente, después de descargar o clonar el repositorio y crear un entorno virtual, se utilizan estos comandos:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

El navegador muestra la aplicación en `http://localhost:8501`.

[Insertar captura del dashboard completo.]

## 2. Preparar y validar los datos

El CSV contiene fecha, ciudad, categoría, producto, cantidad, precio unitario y costo unitario. Cada fila representa una línea de venta. Esta distinción evita confundir el número de filas con el número de pedidos o clientes.

Antes de mostrar resultados, la aplicación revisa las columnas obligatorias, la validez de las fechas y los campos de texto. También comprueba que las cantidades sean enteros positivos y que los importes sean números finitos no negativos. El archivo tiene un límite de 10 MB y 100.000 filas.

Las fechas se normalizan con Pandas y se calculan tres columnas:

```python
df['ventas'] = df['cantidad'] * df['precio_unitario']
df['costo'] = df['cantidad'] * df['costo_unitario']
df['utilidad_bruta'] = df['ventas'] - df['costo']
```

La utilidad mostrada es bruta: no descuenta impuestos ni gastos operativos. El margen se calcula dividiendo la utilidad bruta entre las ventas y multiplicando por cien. Cuando las ventas son cero, la aplicación muestra un margen de cero para evitar una división indefinida.

## 3. Construir indicadores y visualizaciones

El dashboard presenta ventas totales, utilidad bruta, unidades vendidas y margen bruto. Todos se calculan sobre los datos filtrados.

El gráfico de líneas muestra la evolución diaria; las barras horizontales comparan ciudades; el gráfico de dona muestra la participación de las categorías. Un cuarto gráfico compara ventas y utilidad bruta de los diez productos con mayores ventas, o de todos los disponibles si son menos.

Cada visualización responde a una pregunta distinta. La evolución permite identificar variaciones temporales; la comparación por ciudad muestra la distribución geográfica, y la comparación de ventas con utilidad evita evaluar un producto únicamente por su facturación.

[Insertar captura con Tacna seleccionada y explicar el resultado que realmente aparezca.]

## 4. Agregar interacción y exportación

La barra lateral permite seleccionar ciudades, categorías y un intervalo de fechas. Si la selección no contiene registros, se muestra un mensaje claro en lugar de gráficos vacíos. También se puede cargar un CSV propio que respete el esquema de ejemplo.

La pestaña de datos permite revisar las filas y exportar la selección. Para reducir el riesgo de que una hoja de cálculo interprete texto importado como una fórmula, la exportación antepone una comilla a cadenas que comienzan con caracteres de fórmula.

## 5. Automatizar las comprobaciones

Las pruebas verifican cálculos conocidos, entradas inválidas, ventas iguales a cero y protección de texto en la exportación. Además, AppTest ejecuta la interfaz, selecciona Tacna y comprueba que el indicador de ventas coincida con los registros de esa ciudad. Otra comprobación revisa la selección vacía.

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

El archivo `.github/workflows/ci.yml` repite las pruebas automáticamente ante un push a `main` o una solicitud de cambios. Esto constituye la integración continua, o CI.

[Insertar captura de una ejecución real y exitosa de GitHub Actions.]

## 6. Publicar y actualizar automáticamente

En Streamlit Community Cloud se seleccionan el repositorio público, la rama `main` y el archivo `app.py`. Después se inicia el despliegue y se comprueba la URL pública desde una ventana privada.

Una vez enlazado el repositorio, Community Cloud actualiza la aplicación cuando recibe cambios de la rama configurada. Esta es la parte de despliegue continuo, o CD. No es necesario subir manualmente los archivos al servidor en cada modificación.

GitHub Actions y Community Cloud realizan funciones diferentes: el primero comprueba el código; el segundo publica la aplicación. En esta configuración, el alojamiento no espera por sí mismo el resultado de las pruebas. Si se desea impedir que cambios sin validar lleguen a `main`, hay que proteger esa rama y exigir el check de pruebas mediante pull requests.

Para demostrar la automatización, se puede modificar un texto visible, crear un commit, hacer push y comprobar la actualización en la URL pública. Conviene registrar tanto el commit como el resultado publicado.

[Insertar captura de la aplicación alojada con su URL visible.]

## Aprendizajes y limitaciones

El proyecto integra un flujo reproducible desde un CSV hasta una aplicación web. Su alcance es académico: utiliza datos sintéticos, no tiene autenticación ni una base de datos persistente y procesa archivos de tamaño limitado. Los indicadores ayudan a explorar la información, pero no sustituyen un análisis contable completo.

Una ampliación posible sería incorporar una fuente de datos autorizada, registrar pedidos con identificadores y separar descuentos, impuestos y gastos operativos. La versión actual mantiene un esquema pequeño para facilitar su comprensión y reproducción.

## Código, aplicación y video

- Repositorio público: https://github.com/Gino019/ventas360-peru
- Dashboard publicado: [PEGAR URL REAL DE STREAMLIT]
- Video de construcción y demostración, máximo cinco minutos: [PEGAR URL REAL DEL VIDEO]

## Referencias oficiales

- Streamlit: https://docs.streamlit.io/
- Despliegue: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- Actualización de la aplicación: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app
- Pruebas de Streamlit: https://docs.streamlit.io/develop/api-reference/app-testing
- Pandas: https://pandas.pydata.org/docs/
- Plotly: https://plotly.com/python/
- GitHub Actions: https://docs.github.com/en/actions
