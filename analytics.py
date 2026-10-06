import numpy as np
import pandas as pd

REQUIRED = ['fecha', 'ciudad', 'categoria', 'producto', 'cantidad', 'precio_unitario', 'costo_unitario']

def validate_data(df):
    missing = set(REQUIRED) - set(df.columns)
    if missing:
        raise ValueError('Faltan columnas: ' + ', '.join(sorted(missing)))
    df = df[REQUIRED].copy()
    if df.empty:
        raise ValueError('El archivo no contiene ventas.')
    if len(df) > 100000:
        raise ValueError('El límite es 100 000 filas.')
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors='coerce')
    if df['fecha'].isna().any():
        raise ValueError('Usa fechas válidas en formato AAAA-MM-DD.')
    for col in ['ciudad', 'categoria', 'producto']:
        if df[col].isna().any() or df[col].astype(str).str.strip().eq('').any():
            raise ValueError(f'Hay valores vacíos en {col}.')
        df[col] = df[col].astype(str).str.strip()
    for col in ['cantidad', 'precio_unitario', 'costo_unitario']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        if not np.isfinite(df[col]).all() or (df[col] < 0).any():
            raise ValueError(f'{col} debe contener números finitos no negativos.')
    if (df['cantidad'] <= 0).any() or (df['cantidad'] % 1 != 0).any():
        raise ValueError('La cantidad debe ser un entero positivo.')
    df['ventas'] = df['cantidad'] * df['precio_unitario']
    df['costo'] = df['cantidad'] * df['costo_unitario']
    df['utilidad_bruta'] = df['ventas'] - df['costo']
    if not np.isfinite(df[['ventas', 'costo', 'utilidad_bruta']]).all().all():
        raise ValueError('Los importes calculados exceden el rango permitido.')
    return df

def summarize(df):
    sales = float(df['ventas'].sum())
    profit = float(df['utilidad_bruta'].sum())
    return {'ventas': sales, 'utilidad': profit, 'unidades': int(df['cantidad'].sum()),
            'margen': profit / sales * 100 if sales else 0}

def safe_csv(df):
    df = df.copy()
    for col in df.select_dtypes(include=['object', 'string']).columns:
        df[col] = df[col].map(lambda x: "'" + x if isinstance(x, str) and x.lstrip().startswith(('=', '+', '-', '@', '\t', '\r')) else x)
    return df.to_csv(index=False).encode('utf-8-sig')
