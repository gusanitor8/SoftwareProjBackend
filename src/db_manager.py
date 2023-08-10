from config.database import Session
from sqlalchemy import text
from datetime import date
from models import Cuscar, Guia, Remitente, Destino, Paquete


def custom_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()  # Convert date to ISO format
    
##funcion que toma los nombres de las colunnas y las filas y las convierte en un diccionario
def jsonifyResponse(rows, column_names):
    data = [dict(zip(column_names, row)) for row in rows]
    return data
    

def getAnicamView():
    try:
        session = Session()
        view_query = text("SELECT * FROM anicam_table_view")
        result = session.execute(view_query)
        
        # Fetch all data from the result
        rows = result.fetchall()
        column_names = result.keys()  # Extract column names

        # Combine column names and rows into a list of dictionaries
        data = jsonifyResponse(rows, column_names)

        return data
    finally:
        session.close()


def getCuscarView():
    try:
        session = Session()
        query = session.query(Cuscar).all()
        return query
    finally:
        session.close()

def getAnicamViewSql():
    session = Session()
    query = session.query(
        #tabla guia
        Guia.Guia.no_guia,
        Guia.Guia.fecha,

        #tabla remitente
        Remitente.Remitente.compania,
        Remitente.Remitente.contacto,
        Remitente.Remitente.email,
        Remitente.Remitente.direccion,
        Remitente.Remitente.codigo_postal,
        Remitente.Remitente.ciudad,
        Remitente.Remitente.estado,
        Remitente.Remitente.pais,
        Remitente.Remitente.telefono,

        #tabla destino
        Destino.Destino.nombre,
        Destino.Destino.direccion,
        Destino.Destino.codigo_postal,
        Destino.Destino.ciudad,
        Destino.Destino.estado,
        Destino.Destino.pais,
        Destino.Destino.telefono,

        #tabla paquete
        Paquete.Paquete.contenido,
        Paquete.Paquete.piezas,
        Paquete.Paquete.peso_libras,
        Paquete.Paquete.peso_kilos,
        Paquete.Paquete.valor_declarado,
        Paquete.Paquete.news,
        Paquete.Paquete.linea_de_negocio,
        Paquete.Paquete.pre_alerta,
        Paquete.Paquete.guia_externa,
        Paquete.Paquete.precinto,
        Paquete.Paquete.largo,
        Paquete.Paquete.alto,
        Paquete.Paquete.ancho,
        Paquete.Paquete.carrier        
    ).join(Remitente.Remitente, Guia.Guia.no_guia == Remitente.Remitente.No_guia).\
        join(Destino.Destino, Guia.Guia.no_guia == Destino.Destino.No_guia).\
        join(Paquete.Paquete, Guia.Guia.no_guia == Paquete.Paquete.No_guia)
     
    rows = query.all()

    column_names = column_names = [desc['name'] for desc in query.column_descriptions]

    result = jsonifyResponse(rows, column_names)
    return result