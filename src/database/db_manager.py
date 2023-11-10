from config.database import Session
from sqlalchemy import text
from datetime import date
from dataModels.paquete import PaqueteBase
from models.paquete_table import Paquete


# from models import Cuscar, Guia, Remitente, Destino, Paquete, Oea, Costeo

def convert_and_format_date(date_str):
    # Manejo de nulos
    if date_str is None:
        return None

    # Reemplazar '/' con '-' para manejar ambos formatos
    date_str = date_str.replace('/', '-')

    # Convertir la cadena a un objeto de fecha
    date_obj = date.strptime(date_str, '%d-%m-%Y').date()

    # Formatear el objeto de fecha al formato deseado (en este caso, dd-mm-yyyy)
    formatted_date = date_obj.strftime('%d/%m/%Y')

    return formatted_date


def custom_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()  # Convert date to ISO format


##funcion que toma los nombres de las colunnas y las filas y las convierte en un diccionario
def jsonifyResponse(rows, column_names):
    data = [dict(zip(column_names, row)) for row in rows]
    return data


def upload_paquete(paquete: PaqueteBase):
    session = Session()

    try:
        new_paquete = Paquete(
            id_paquete=paquete.id_paquete,
            factura=paquete.factura,
            fecha_orden=paquete.fecha_orden,
            contenido=paquete.contenido,
            descripcion=paquete.descripcion,
            alto=paquete.alto,
            ancho=paquete.ancho,
            largo=paquete.largo,
            peso_libras=paquete.peso_libras,
            valor_dolar=paquete.valor_dolar,
            unidades=paquete.unidades,
            direccion_casillero=paquete.direccion_casillero,
            empresa_remitente=paquete.empresa_remitente,
            cliente_nombre=paquete.cliente_nombre,
            cliente_telefono=paquete.cliente_telefono,
            cliente_email=paquete.cliente_email,
            cliente_direccion=paquete.cliente_direccion
        )

        session.add(new_paquete)

    except Exception as e:
        raise e

    finally:
        session.close()
