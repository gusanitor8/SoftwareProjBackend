from src.database.db_package import invoice_search

def test_get_consolidado():
    con = invoice_search(1)
    hola = "hola"