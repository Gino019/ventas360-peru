from pathlib import Path
import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest
from analytics import validate_data, summarize, safe_csv

ROOT = Path(__file__).resolve().parents[1]

def sample():
    return pd.DataFrame([dict(fecha='2026-01-01',ciudad='Tacna',categoria='Tecnología',producto='Mouse',cantidad=2,precio_unitario=50,costo_unitario=30)])

def test_math():
    assert summarize(validate_data(sample())) == {'ventas':100,'utilidad':40,'unidades':2,'margen':40}

@pytest.mark.parametrize('col,value', [('cantidad',1.5),('cantidad',-1),('precio_unitario',float('inf')),('fecha','no-fecha'),('ciudad','')])
def test_rejects_bad_data(col,value):
    df = sample(); df[col] = value
    with pytest.raises(ValueError): validate_data(df)

def test_zero_sales():
    df=sample(); df['precio_unitario']=0
    assert summarize(validate_data(df))['margen'] == 0

def test_export_formula():
    df=sample(); df['producto']='=1+1'
    assert "'=1+1" in safe_csv(df).decode('utf-8-sig')

def test_dashboard_filters():
    at = AppTest.from_file(str(ROOT/'app.py')).run(timeout=30)
    assert not at.exception
    assert len(at.metric) == 4
    at.multiselect[0].set_value(['Tacna']).run()
    expected = validate_data(pd.read_csv(ROOT/'data/ventas_demo.csv'))
    sales = expected.loc[expected.ciudad.eq('Tacna'),'ventas'].sum()
    assert at.metric[0].value == f'S/ {sales:,.2f}'
    at.multiselect[0].set_value([]).run()
    assert not at.exception
    assert len(at.warning) == 1
