# Guion de video — objetivo: 4 minutos 40 segundos

Graba la pantalla con tu voz. Prepara las pestañas del editor, GitHub Actions y la app pública. Realiza antes la instalación y el primer despliegue para no consumir el tiempo del video esperando. Di las partes de publicación solo cuando ya estén verificadas.

## 0:00–0:25 | Presentación
Pantalla: dashboard completo.

«Hola, soy Eduardo Gino Flores Navarro. En este video presentaré la construcción de Ventas360 Perú, un dashboard con Python y Streamlit. Permite explorar ventas por ciudad, categoría y fechas. Los datos de esta demostración son sintéticos y no corresponden a ventas reales.»

## 0:25–1:00 | Estructura y datos
Pantalla: editor, estructura del proyecto y CSV.

«El proyecto separa la interfaz en app.py y los cálculos en analytics.py. En data se encuentra el archivo de ejemplo con mil doscientas líneas de venta. Cada registro incluye fecha, ciudad, producto, cantidad, precio y costo. Antes de procesarlo, validamos las columnas, las fechas y los valores numéricos.»

## 1:00–1:40 | Construcción
Pantalla: fórmulas en analytics.py, comando de ejecución y bloques de gráficos en app.py.

«Con Pandas calculamos las ventas multiplicando cantidad por precio unitario. La utilidad bruta se obtiene restando el costo de los productos. Después agrupamos los resultados por fecha, ciudad y producto. Streamlit muestra los controles y los indicadores; Plotly construye las visualizaciones interactivas. Para iniciar la aplicación ejecutamos python, guion m, streamlit run app.py.»

## 1:40–2:25 | Demostración
Pantalla: selecciona Tacna, cambia categoría, abre datos y descarga CSV.

«Estos cuatro indicadores resumen las ventas, la utilidad bruta, las unidades y el margen. Al seleccionar Tacna, todos los gráficos se actualizan con los registros de esa ciudad. La línea muestra la evolución diaria, las barras comparan ciudades y la dona presenta la distribución por categoría. También podemos revisar las filas y descargar el resultado filtrado. La utilidad es bruta porque no considera impuestos ni gastos operativos.»

## 2:25–3:00 | Repositorio y pruebas
Pantalla: repositorio público, historial de commits y ejecución exitosa de Actions.

«El código completo está en este repositorio público. Los commits separan la implementación, las pruebas y la documentación. GitHub Actions ejecuta pruebas automáticamente. Se verifican las fórmulas, los archivos inválidos y el comportamiento de los filtros de la interfaz. Esta parte corresponde a integración continua.»

## 3:00–4:10 | Despliegue automático
Pantalla: configuración de Community Cloud; cambio pequeño de un subtítulo, commit/push y URL publicada.

«Para el alojamiento conectamos el repositorio a Streamlit Community Cloud, seleccionamos main y el archivo app.py. Después del primer despliegue, los nuevos cambios en la rama configurada actualizan la aplicación automáticamente. Aquí cambio este texto, guardo un commit y lo publico en GitHub. Ahora comprobamos el cambio en la dirección pública. Community Cloud realiza el despliegue; GitHub Actions ejecuta las pruebas. Son procesos distintos.»

Si tarda, recorta la espera e indica “después del despliegue”. No muestres tokens ni configuraciones privadas. Si aún no se publicó, no afirmes que funciona: completa ese paso antes de grabar esta sección.

## 4:10–4:40 | Cierre
Pantalla: artículo Medium y enlaces reales de entrega.

«Este proyecto muestra cómo transformar un CSV en un dashboard interactivo y mantenerlo publicado mediante un repositorio. En el artículo de Medium explico los pasos, las herramientas y las limitaciones. Allí están los enlaces al código público, a la aplicación y a este video. Gracias.»

# Publicar el artículo en Medium

1. Copia el título y el contenido de articulo_medium.md en una historia nueva.
2. Quita la nota de borrador y sustituye todos los marcadores por enlaces y capturas reales.
3. Conserva los bloques de código con formato legible; revisa las listas y subtítulos.
4. Agrega etiquetas relacionadas, como Python, Data Visualization, Streamlit y GitHub.
5. Publica y comprueba el enlace desde una ventana privada.
6. Cada integrante debe publicar su propio artículo según el enunciado; puede describir su aporte y sus aprendizajes.

# Lista final de entrega

- Repositorio público accesible sin iniciar sesión.
- App pública funcional y filtros comprobados.
- GitHub Actions ejecutado correctamente.
- Cambio por push reflejado en la app como evidencia de automatización.
- Video público de duración igual o menor a 5:00.
- Artículo de Medium con los tres enlaces reales.
