from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st
from analytics import validate_data, summarize, safe_csv

st.set_page_config(page_title='Ventas360 Perú | Dashboard', page_icon='📊', layout='wide')
st.title('Ventas360 Perú')
st.caption('Explora ventas, productos y ciudades · Streamlit + Pandas + Plotly')
with st.sidebar:
    st.header('Panel de control')
    upload = st.file_uploader('Importar ventas CSV (máximo 10 MB)', type=['csv'])
    st.caption('Fechas: AAAA-MM-DD · Importes: soles · Separador: coma')
    st.download_button('Descargar CSV de ejemplo', (Path(__file__).parent/'data/ventas_demo.csv').read_bytes(), 'ventas_demo.csv', 'text/csv')
try:
    if upload is not None and upload.size > 10 * 1024 * 1024:
        raise ValueError('El archivo supera 10 MB.')
    df = validate_data(pd.read_csv(upload if upload is not None else Path(__file__).parent/'data/ventas_demo.csv'))
except (ValueError, UnicodeError, pd.errors.ParserError) as exc:
    st.error(f'No se pudo cargar el archivo: {exc}')
    st.stop()
if upload is None:
    st.info('Datos sintéticos para demostración académica. No representan ventas reales.')
else:
    st.caption('Fuente: CSV cargado en esta sesión. No se guarda en el repositorio.')
with st.sidebar:
    cities = st.multiselect('Ciudades', sorted(df.ciudad.unique()), default=sorted(df.ciudad.unique()))
    categories = st.multiselect('Categorías', sorted(df.categoria.unique()), default=sorted(df.categoria.unique()))
    start, end = df.fecha.min().date(), df.fecha.max().date()
    dates = st.date_input('Periodo', value=(start,end), min_value=start, max_value=end)
if len(dates) != 2:
    st.warning('Selecciona una fecha inicial y una final.')
    st.stop()
filtered = df[df.ciudad.isin(cities) & df.categoria.isin(categories) & df.fecha.between(pd.Timestamp(dates[0]), pd.Timestamp(dates[1]))]
if filtered.empty:
    st.warning('No hay ventas con estos filtros. Selecciona otra ciudad, categoría o periodo.')
    st.stop()
summary = summarize(filtered)
for col, label, value in zip(st.columns(4), ['Ventas', 'Utilidad bruta', 'Unidades', 'Margen bruto'], [f"S/ {summary['ventas']:,.2f}",f"S/ {summary['utilidad']:,.2f}",f"{summary['unidades']:,}",f"{summary['margen']:.1f}%"]):
    col.metric(label,value)
st.caption('Utilidad bruta = ventas − costo de productos. No incluye impuestos ni gastos operativos. Cada fila representa una línea de venta.')
colors = ['#2563eb','#14b8a6','#f59e0b','#a855f7']
chart_tab, data_tab = st.tabs(['Visualizaciones', 'Datos y exportación'])
with chart_tab:
    daily = filtered.groupby('fecha',as_index=False)['ventas'].sum()
    st.plotly_chart(px.line(daily, x='fecha',y='ventas',markers=True,title='Evolución diaria de ventas',color_discrete_sequence=colors,labels={'fecha':'Fecha','ventas':'Ventas (S/)'}),use_container_width=True)
    a,b = st.columns(2)
    with a:
        city = filtered.groupby('ciudad',as_index=False)['ventas'].sum().sort_values('ventas')
        st.plotly_chart(px.bar(city,x='ventas',y='ciudad',orientation='h',title='Ventas por ciudad',color_discrete_sequence=colors),use_container_width=True)
    with b:
        category = filtered.groupby('categoria',as_index=False)['ventas'].sum()
        if category.ventas.sum() > 0:
            st.plotly_chart(px.pie(category,names='categoria',values='ventas',hole=.6,title='Participación por categoría',color_discrete_sequence=colors),use_container_width=True)
        else:
            st.info('La participación no se calcula cuando las ventas son cero.')
    top = filtered.groupby('producto',as_index=False)[['ventas','utilidad_bruta']].sum().nlargest(10,'ventas')
    st.plotly_chart(px.bar(top,x='producto',y=['ventas','utilidad_bruta'],barmode='group',title='Productos: ventas y utilidad bruta',color_discrete_sequence=colors),use_container_width=True)
with data_tab:
    st.write(f'{len(filtered):,} líneas de venta seleccionadas')
    st.dataframe(filtered,hide_index=True,use_container_width=True)
    st.download_button('Descargar datos filtrados',safe_csv(filtered),'ventas_filtradas.csv','text/csv')
with st.expander('Formato de importación y metodología'):
    st.write('Columnas obligatorias: fecha, ciudad, categoria, producto, cantidad, precio_unitario, costo_unitario. Cantidad: entero positivo; precios y costos: números no negativos, con punto decimal. Máximo 100 000 filas.')
    st.write('Ventas = cantidad × precio unitario. Margen bruto = utilidad bruta / ventas × 100. Si las ventas son cero, se muestra 0%. Los filtros afectan todos los indicadores y gráficos.')
