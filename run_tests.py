from src.database.db_package import get_consolidado

def test_get_consolidado():
    con = get_consolidado(1)
    hola = "hola"