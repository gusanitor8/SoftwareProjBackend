from config.database import Session
from dataModels.revision_sat import RevisionSatBase
from models.revision_sat_table import RevisionSat
from models.paquete_table import Paquete
from models.impuesto_table import Impuesto
from typing import Dict, Any
from sqlalchemy.exc import IntegrityError, DataError, OperationalError

def registrar_revision(revision: RevisionSatBase, id_paquete: int, cambios: Dict[str, Any]):
    
    try:
        
        session = Session()

        # Obtener datos actuales del paquete e impuesto
        paquete_actual = session.query(Paquete).filter(Paquete.id_paquete == id_paquete).one()
        impuesto_actual = session.query(Impuesto).filter(Impuesto.paquete_id == id_paquete).one()

        # Convertir a diccionarios
        paquete_dict = {column.name: getattr(paquete_actual, column.name) for column in paquete_actual.__table__.columns}
        impuesto_dict = {column.name: getattr(impuesto_actual, column.name) for column in impuesto_actual.__table__.columns}

        # Combinar los diccionarios de paquete e impuesto
        registro_actual = {**paquete_dict, **impuesto_dict}

        # Crear registro de RevisionSat
        revision_obj = RevisionSat(
            selectivo_id = revision.selectivo_id,
            registros_antiguos = registro_actual,
            registros_nuevos = cambios,
            usuario_id = revision.usuario_id
        )

        session.add(revision_obj)
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
