from ..src.data_manipulation import *
import pandas as pd


def test_createExcelFile():
    df = pd.DataFrame({"Pruebita": "Hola", "Pruebita2": "Hola2"}, index=[0])
    result = createExcelFile(df)

    assert result is not None

def test_excelToDictList():
    df = pd.DataFrame({"Prueba": ["Primera Fila", "Segunda Fila"], 
                       "Prueba2": ["Primera fila col 2", "Segunda Fila col 2"]})
    excel = createExcelFile(df)
    dict_res = excelToDictList(excel)    
    
    assert dict_res == df.to_dict(orient='records')
   
def test_dictListToDataframe():
    list_of_dicts = [{"Prueba": "Primera Fila", "Prueba2": "Primera fila col 2"},
                     {"Prueba": "Segunda Fila", "Prueba2": "Segunda Fila col 2"}]
    dict = {"Prueba": ["Primera Fila", "Segunda Fila"], 
            "Prueba2": ["Primera fila col 2", "Segunda Fila col 2"]}

    df_dict = pd.DataFrame(dict)
    df_dict_list = dictListToDataframe(list_of_dicts)
    
    assert df_dict.equals(df_dict_list)

def test_dataFrameToDictList():
    dict = {"Prueba": ["Primera Fila", "Segunda Fila"], 
            "Prueba2": ["Primera fila col 2", "Segunda Fila col 2"]}
    list_of_dicts = [{"Prueba": "Primera Fila", "Prueba2": "Primera fila col 2"},
                     {"Prueba": "Segunda Fila", "Prueba2": "Segunda Fila col 2"}]
     
    df_dict = pd.DataFrame(dict)
    df_dict_list = dataFrameToDictList(df_dict)
    
    assert df_dict_list == list_of_dicts
    

