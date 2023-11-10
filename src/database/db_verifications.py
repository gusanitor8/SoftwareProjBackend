from config.database import Session
from models.consolidacion_table import Consolidacion
from models.selectivo_sat_table import SelectivoSAT
from src.Selectivos import Selectivos

def get_selective(paquete_id: int):
    try:
        session = Session()
        consolidado_id = session.query(Consolidacion.consolidado_id).filter(Consolidacion.paquete_id == paquete_id).first()
        selective = session.query(SelectivoSAT.selectivo_asignado).filter(SelectivoSAT.consolidado_id == consolidado_id).first()

        if selective is None:
            return None
        
        return selective

    finally:
        session.close()


def check_red_selective(paquete_id: int, required_Selective: Selectivos) -> bool:
    """
    Esta funcion regresa verdadero si el selectivo es verde, falso si es rojo
    """
    selective = get_selective(paquete_id)

    if selective is not None:
        if selective == required_Selective.value:
            return True

    return False