from src.db_manager import *

def test_getAnicamView():
    result = getAnicamView()
    print(result)

    assert result is not None

def test_getCuscarView():
    result = getCuscarView()
    print(result)

    assert result is not None
    