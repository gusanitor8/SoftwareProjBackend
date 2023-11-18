from config.database import Session
from dataModels.gasto import GastoBase
from models.gasto_table import Gasto
from models.impuesto_table import Impuesto
from models.paquete_table import Paquete
from models.seguimiento_paquete_table import SeguimientoPaquete
from sqlalchemy.exc import IntegrityError, DataError, OperationalError

def carga_gastos(gastos: GastoBase, user: int):
    try:
        session = Session()

        paquete_impuesto = session.query(Impuesto).filter(Impuesto.paquete_id == gastos.paquete_id).one()
        paquete = session.query(Paquete).filter(Paquete.id_paquete == gastos.paquete_id).one()

        cambioDolar = 7.98

        # Obtencion de datos autogenerados basados en data de paquete y sus impuestos
        iva_quetzal = paquete_impuesto.monto_iva_dolar * cambioDolar
        dai_quetzal = paquete_impuesto.monto_dai_dolar * cambioDolar
        valor_producto_quetzal = paquete.valor_producto_dolar * cambioDolar
        total = iva_quetzal + dai_quetzal + valor_producto_quetzal + gastos.monto_flete + gastos.monto_combex
        
        # Creacion e insercion de un nuevo gasto asociado a paquete
        gasto_obj = Gasto(
            # id_gasto autogenerado
            paquete_id = gastos.paquete_id,
            monto_iva_quetzal = iva_quetzal,
            monto_dai_quetzal = dai_quetzal,
            monto_flete = gastos.monto_flete,
            monto_combex = gastos.monto_combex,
            valor_quetzal = valor_producto_quetzal,
            gasto_total =  total
        )

        # Insertar el nuevo impuesto en la base de datos
        session.add(gasto_obj)


        # Crear seguimiento para cada paquete en el consolidado
        seguimiento_obj = SeguimientoPaquete(
            estado_actual='en bodega',
                motivo_cambio='Listo para entrega',
                paquete_id= paquete.id_paquete,
                usuario_id= user
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