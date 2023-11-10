from config.database import Session
from dataModels.impuesto import ImpuestoBase
from models.impuesto_table import Impuesto
from models.paquete_table import Paquete
from sqlalchemy.exc import IntegrityError, DataError, OperationalError




def carga_impuestos(impuesto: ImpuestoBase):
    try:
        session = Session()

        paquete = session.query(Paquete).filter(Paquete.id_paquete == impuesto.paquete_id).one()
        
        iva_dolar = paquete.valor_producto_dolar * 0.12
        dai_dolar = paquete.valor_producto_dolar * (impuesto.dai_porcentaje / 100)

        # Crear el objeto Impuesto
        impuesto_obj = Impuesto(
            # id_impuesto autogenerado
            paquete_id = impuesto.paquete_id,
            monto_iva_dolar = iva_dolar,
            dai_porcentaje = impuesto.dai_porcentaje,
            monto_dai_dolar = dai_dolar,
            poliza = impuesto.poliza,
            partida = impuesto.partida,
            consignatario = impuesto.consignatario
            # fecha_impuesto autogenerada
        )
        
        # Insertar el nuevo impuesto en la base de datos
        session.add(impuesto_obj)

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
        # Asegurarse de cerrar la sesion de la base de datos
        session.close()