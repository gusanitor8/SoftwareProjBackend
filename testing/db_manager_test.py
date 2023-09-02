from src.db_manager import *

def test_getAnicamView():
    result = getAnicamView()
    print(result)

    assert result is not None

def test_getCuscarView():
    result = getCuscarView()
    print(result)

    assert result is not None


def test_getAnicamViewSql():
    result = getAnicamViewSql()
    print(result)    
    assert result is not None    
    

def test_updateAnicamData():
    register = {        
        "fecha": "string",
        "REMITENTE_compania": "string",
        "REMITENTE_contacto": "string",
        "REMITENTE_email": "string",
        "REMITENTE_direccion": "string",
        "REMITENTE_codigo_postal": 0,
        "REMITENTE_ciudad": "string",
        "REMITENTE_estado": "string",
        "REMITENTE_pais": "string",
        "REMITENTE_telefono": 0,
        "DESTINO_nombre": "string",
        "DESTINO_direccion": "string",
        "DESTINO_codigo_postal": 0,
        "DESTINO_ciudad": "string",
        "DESTINO_estado": "string",
        "DESTINO_pais": "string",
        "DESTINO_telefono": 0,
        "alto": 0,
        "ancho": 0,
        "carrier": "string",
        "contenido": "string",
        "guia_externa": 0,
        "largo": 0,
        "linea_de_negocio": "string",
        "news": "string",
        "peso_kilos": 0,
        "peso_libras": 0,
        "piezas": 0,
        "pre_alerta": 0,
        "precinto": "string",
        "valor_declarado": 0
    }

    result = updateAnicamData(**register)
    print(result)    
    assert result is True