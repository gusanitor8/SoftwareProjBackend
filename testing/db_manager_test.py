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
    
def test_getFinancesViewSql():
    result = getFinancesViewSql()
    print(result)
    assert result is not None
    
def test_updateAnicamData():
<<<<<<< HEAD
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
=======
    register = {
        "no_guia": 888,
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
>>>>>>> DBDevelopmentOps
    }

    result = updateAnicamData(**register)
    print(result)    
    assert result is True


