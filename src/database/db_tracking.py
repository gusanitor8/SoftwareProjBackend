from config.database import Session
from dataModels.paquete import PaqueteBase
from dataModels.seguimiento_paquete import SeguimientoPaqueteBase
from models.seguimiento_paquete_table import SeguimientoPaquete
from sqlalchemy.exc import IntegrityError, DataError, OperationalError

def seguimiento_paquete(seguimiento: SeguimientoPaqueteBase):
    try:
        session = Session()

        # Creacion e insercion de un registro de seguimiento de paquete
        seguimiento_obj = SeguimientoPaquete(
            # id_seguimiento autogenerado
            estado_actual = seguimiento.estado_actual,
            motivo_cambio = seguimiento.motivo_cambio,
            paquete_id = seguimiento.paquete_id,
            # fecha_actualizacion autogenerada
            usuario_id = seguimiento.usuario_id
        )
        session.add(seguimiento_obj)
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