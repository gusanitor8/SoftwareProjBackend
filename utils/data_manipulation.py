import pandas as pd
from config.database import Session
from io import BytesIO
from sqlalchemy import text, MetaData, Table
from config.database import engine
from datetime import datetime

def read_excel(file):
    df = pd.read_excel(BytesIO(file))
    column_names = df.columns.tolist() 

    if validate_columns(column_names, "guia"):   #cambiar nombre de la tabla
        return df  
    return df

def validate_columns(columns, table_name):
    table_columns = get_columns(table_name)
    return table_columns == columns



def get_columns(table_name):
    metadata = MetaData()
    metadata.reflect(bind=engine)    
    table = Table(table_name, metadata, autoload=True, autoload_with=engine)
    column_names = table.columns.keys()
    return column_names

def make_excel():
    data = {"Pruebita": "Hola", "Pruebita2": "Hola2"}
    df = pd.DataFrame(data, index=[0])
    excel_writer = BytesIO()
    df.to_excel(excel_writer, index=False, engine="openpyxl")
    excel_writer.seek(0)
    return excel_writer
    
def test_function():
    params = {"p_fecha": datetime(2021, 1, 1).date()}
    SQLquery = """SELECT test_procedure(
        CAST(:p_fecha AS DATE)
    )"""
    db = Session()
    result = db.execute(text(SQLquery), params)
    db.commit()
    return result
    