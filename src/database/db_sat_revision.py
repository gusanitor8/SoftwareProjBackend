from config.database import Session
from dataModels.revision_sat import RevisionSatBase
from models.revision_sat_table import RevisionSat
from models.paquete_table import Paquete
from models.impuesto_table import Impuesto
from models.gasto_table import Gasto
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


def actualizar_paquete_impuesto(paquete_id: int, cambios: Dict[str, Any]):
    session = Session()
    try:
        paquete = session.query(Paquete).filter(Paquete.id_paquete == paquete_id).one()
        impuesto = session.query(Impuesto).filter(Impuesto.paquete_id == paquete_id).one()

        # Actualizar datos del paquete
        for key, value in cambios['paquete'].items():
            if hasattr(paquete, key):
                setattr(paquete, key, value)

        # Actualizar datos del impuesto
        for key, value in cambios['impuesto'].items():
            if hasattr(impuesto, key):
                setattr(impuesto, key, value)

        # Aquí puedes llamar a funciones para recalcular valores dependientes
        recalcular_valores_dependientes(paquete, impuesto)

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


def recalcular_valores_dependientes(paquete: Paquete, impuesto: Impuesto):
    session = Session()
    try:
        # recalcular valores dependientes en Gasto
        cambioDolar = 7.98

        # Recalcular valores para el impuesto
        impuesto.monto_iva_dolar = paquete.valor_producto_dolar * 0.12
        impuesto.monto_dai_dolar = paquete.valor_producto_dolar * (impuesto.dai_porcentaje / 100)
        
        # Buscar y actualizar el gasto asociado, si existe
        gasto = session.query(Gasto).filter(Gasto.paquete_id == paquete.id_paquete).one_or_none()
        if gasto:
            gasto.monto_iva_quetzal = impuesto.monto_iva_dolar * cambioDolar
            gasto.monto_dai_quetzal = impuesto.monto_dai_dolar * cambioDolar
            gasto.valor_quetzal = paquete.valor_producto_dolar * cambioDolar
            gasto.gasto_total = gasto.monto_iva_quetzal + gasto.monto_dai_quetzal + gasto.monto_flete + gasto.monto_combex

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