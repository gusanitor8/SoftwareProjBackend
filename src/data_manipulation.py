import pandas as pd
from io import BytesIO

#Crea un archivo de excel a partir de un dataframe
def createExcelFile(df: pd.DataFrame) -> bytes:
    excel_writer = BytesIO()
    df.to_excel(excel_writer, index=False, engine="openpyxl")
    excel_writer.seek(0)
    return excel_writer.getvalue()


#Crea un diccionario a partir de un archivo de excel
def excelToDictList(file: BytesIO) -> list[dict]:
    df = pd.read_excel(file)
    df = df.dropna(how='all')
    resulting_dict = df.to_dict(orient='records')
    return resulting_dict


#Devuelve un dataframe a partir de una lista de diccionarios
def dictListToDataframe(list_of_dicts: dict) -> pd.DataFrame:
    df = pd.DataFrame(list_of_dicts)
    return df


#Devuelve una lista de diccionarios a partir de un dataframe
def dataFrameToDictList(df: pd.DataFrame) -> [dict]:
    return df.to_dict(orient='records')
