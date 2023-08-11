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
        "no_guia": 333,
        "Fecha_guia": "2023-07-21",
        "REMITENTE_compania": "jsddasd",
        "REMITENTE_contacto": "sadasd",
        "REMITENTE_email": "updateTest@test.com",
        "REMITENTE_direccion": "asdasd123",
        "REMITENTE_codigo_postal": 9001,
        "REMITENTE_ciudad": "guatemala",
        "REMITENTE_estado": "asddasda",
        "REMITENTE_pais": "guatemala",
        "REMITENTE_telefono": 000000,
        "DESTINO_nombre": "ola",
        "DESTINO_direccion": "ola",
        "DESTINO_codigo_postal": 9008,
        "DESTINO_ciudad": "ola",
        "DESTINO_estado": "ola",
        "DESTINO_pais": "ola",
        "DESTINO_telefono": 231453392,
        "contenido": "qsda",
        "piezas": 123,
        "peso_libras": 12,
        "peso_kilos": 34,
        "valor_declarado": 1,
        "news": "fsd",
        "linea_de_negocio": "dasd",
        "pre_alerta": "jjj",
        "guia_externa": "jjjsdf",
        "precinto": "nkasd",
        "largo": 12,
        "alto": 12,
        "ancho": 12,
        "carrier": "dasds"
    }

    result = updateAnicamData(**register)
    print(result)    
    assert result is True