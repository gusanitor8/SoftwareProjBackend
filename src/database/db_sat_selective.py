from config.database import Session
from dataModels.selectivo_sat import SelectivoSatBase
from models.selectivo_sat_table import SelectivoSAT
from models.consolidacion_table import Consolidacion
from models.seguimiento_paquete_table import SeguimientoPaquete
from sqlalchemy.exc import IntegrityError, DataError, OperationalError
from typing import List

def carga_selectivo(selectivo: SelectivoSatBase, user: int):
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

        paquetes_en_consolidado = session.query(Consolidacion).filter(Consolidacion.consolidado_id == selectivo.consolidado_id).all()

        if selectivo_obj.selectivo_asignado == 'Verde':
            
            # Crear seguimiento para cada paquete en el consolidado
            for consolidacion in paquetes_en_consolidado:
                seguimiento_obj = SeguimientoPaquete(
                    estado_actual='liberado',
                    motivo_cambio='Asignacion de Selectivo VERDE por SAT',
                    paquete_id = consolidacion.paquete_id,
                    usuario_id= user
                )
                session.add(seguimiento_obj)

        if selectivo_obj.selectivo_asignado == 'Rojo':
            # Crear seguimiento para cada paquete en el consolidado
            for consolidacion in paquetes_en_consolidado:
                seguimiento_obj = SeguimientoPaquete(
                    estado_actual='revision SAT',
                    motivo_cambio='Asignacion de Selectivo Rojo por SAT',
                    paquete_id = consolidacion.paquete_id,
                    usuario_id = user
                )
                session.add(seguimiento_obj)



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