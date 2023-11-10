from config.database import Session
from dataModels.selectivo_sat import SelectivoSatBase
from models.selectivo_sat_table import SelectivoSAT
from sqlalchemy.exc import IntegrityError, DataError, OperationalError
from typing import List

def carga_selectivo(selectivo: SelectivoSatBase):
    try:
        session = Session()

        # Creacion e insercion de una nueva asignacion de selectivo SAT
        selectivo_obj = SelectivoSAT(
            # id_selectivo autogenerado
            consolidado_id = selectivo.consolidado_id,
            # fecha_asignacion autogenerada
            selectivo_asignado = selectivo.selectivo_asignado
        )
        session.add(selectivo_obj)
        session.commit()


    except IntegrityError as e:
        session.rollback()
        raise ValueError("Error de integridad: posible registro duplicado o violacion de restricciones.") from e

    except DataError as e:
        session.rollback()
        raise ValueError("Error de datos: campos nulos, incompletos o tipo de datos inadecuado.") from e

    except OperationalError as e:
        session.rollback()
        raise Exception("Error operacional en la base de datos.") from e

    except Exception as e:
        session.rollback()
        raise Exception(f"Error inesperado: {str(e)}") from e

    finally:
        session.close()