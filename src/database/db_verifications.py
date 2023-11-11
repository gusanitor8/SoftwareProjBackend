from config.database import Session
from models.consolidacion_table import Consolidacion
from models.selectivo_sat_table import SelectivoSAT
from src.Selectivos import Selectivos

def get_selective(paquete_id: int):
    try:
        session = Session()
        consolidacion = session.query(Consolidacion).filter(Consolidacion.paquete_id == paquete_id).first()
        consolidado_id = consolidacion.consolidado_id
        selectivoSat = session.query(SelectivoSAT).filter(SelectivoSAT.consolidado_id == consolidado_id).first()
        selectivo = selectivoSat.selectivo_asignado

        if selectivo is None:
            return None
        
        return selectivo

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