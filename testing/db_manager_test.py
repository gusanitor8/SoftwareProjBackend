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
    register = {
        "no_guia": 888,
        "Fecha_guia": "04-09-2023",
        "REMITENTE_compania": "jsddasd",
        "REMITENTE_contacto": "sadasd",
        "REMITENTE_email": "updateTest@test.com",
        "REMITENTE_direccion": "asdasd123",
        "REMITENTE_codigo_postal": 9001,
        "REMITENTE_ciudad": "guatemala",
        "REMITENTE_estado": "asddasda",
        "REMITENTE_pais": "guatemala",
        "REMITENTE_telefono": 10000,
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


def test_updateFinancesData():
    register = {
        "No_guia": 123,
        "codigo": "ABC",
        "courier": "DHL",
        "correlativo": 1,
        "consignatario": "John",
        "libras_a_facturar": 10.5,
        "peso_real_lb": 10.0,
        "peso_vol_lb": 11.0,
        "descripcion_costeo": "Test",
        "cobro_flete": 5.0,
        "ultima_milla": 2.0,
        "gestion_aduana": 1.0,
        "manejo_almacenaje": 3.0,
        "descuentos": 0.5,
        "DAI": 0.2,
        "IVA": 0.1,
        "Numero_de_Declaracion": 456,
        "Declaracion": "Test Declaration",
        "Selectivo": "Green"
    }
    result = updateFinancesData(**register)
    print(result)
    assert result is True


