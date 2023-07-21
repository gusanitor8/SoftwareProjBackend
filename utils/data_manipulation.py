import pandas as pd
from io import BytesIO

def read_excel(file):
    df = pd.read_excel(BytesIO(file))
    return df

def make_excel():
    data = {"Pruebita": "Hola", "Pruebita2": "Hola2"}
    df = pd.DataFrame(data, index=[0])
    excel_writer = BytesIO()
    df.to_excel(excel_writer, index=False, engine="openpyxl")
    excel_writer.seek(0)
    return excel_writer
    
    