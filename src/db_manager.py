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


def updateAnicamData(**kwargs):
    session = Session()
    try:
        # Verificamos si la guía existe
        guia = session.query(Guia.Guia).filter(Guia.Guia.no_guia == kwargs.get("no_guia")).first()
        
        # Si la guía existe, hacemos los updates
        if guia:
            # Actualizamos los datos de la guia
            guia.fecha = kwargs.get("Fecha_guia", guia.fecha)
            
            remitente = session.query(Remitente.Remitente).filter(Remitente.Remitente.No_guia == kwargs.get("no_guia")).first()
            if remitente:
                # Actualizamos los datos del remitente
                remitente.compania = kwargs.get("REMITENTE_compania", remitente.compania)
                remitente.contacto = kwargs.get("REMITENTE_contacto", remitente.contacto)
                remitente.email = kwargs.get("REMITENTE_email", remitente.email)
                remitente.direccion = kwargs.get("REMITENTE_direccion", remitente.direccion)
                remitente.codigo_postal = kwargs.get("REMITENTE_codigo_postal", remitente.codigo_postal)
                remitente.ciudad = kwargs.get("REMITENTE_ciudad", remitente.ciudad)
                remitente.estado = kwargs.get("REMITENTE_estado", remitente.estado)
                remitente.pais = kwargs.get("REMITENTE_pais", remitente.pais)
                remitente.telefono = kwargs.get("REMITENTE_telefono", remitente.telefono)

                
            destino = session.query(Destino.Destino).filter(Destino.Destino.No_guia == kwargs.get("no_guia")).first()
            if destino:
                # Actualizamos los datos del destino
                destino.nombre = kwargs.get("DESTINO_nombre", destino.nombre)
                destino.direccion = kwargs.get("DESTINO_direccion", destino.direccion)
                destino.codigo_postal = kwargs.get("DESTINO_codigo_postal", destino.codigo_postal)
                destino.ciudad = kwargs.get("DESTINO_ciudad", destino.ciudad)
                destino.estado = kwargs.get("DESTINO_estado", destino.estado)
                destino.pais = kwargs.get("DESTINO_pais", destino.pais)
                destino.telefono = kwargs.get("DESTINO_telefono", destino.telefono)
                
            paquete = session.query(Paquete.Paquete).filter(Paquete.Paquete.No_guia == kwargs.get("no_guia")).first()
            if paquete:
                # Actualizamos los datos del paquete
                paquete.contenido = kwargs.get("contenido", paquete.contenido)
                paquete.piezas = kwargs.get("piezas", paquete.piezas)
                paquete.peso_libras = kwargs.get("peso_libras", paquete.peso_libras)
                paquete.peso_kilos = kwargs.get("peso_kilos", paquete.peso_kilos)
                paquete.valor_declarado = kwargs.get("valor_declarado", paquete.valor_declarado)
                paquete.news = kwargs.get("news", paquete.news)
                paquete.linea_de_negocio = kwargs.get("linea_de_negocio", paquete.linea_de_negocio)
                paquete.pre_alerta = kwargs.get("pre_alerta", paquete.pre_alerta)
                paquete.guia_externa = kwargs.get("guia_externa", paquete.guia_externa)
                paquete.precinto = kwargs.get("precinto", paquete.precinto)
                paquete.largo = kwargs.get("largo", paquete.largo)
                paquete.alto = kwargs.get("alto", paquete.alto)
                paquete.ancho = kwargs.get("ancho", paquete.ancho)
                paquete.carrier = kwargs.get("carrier", paquete.carrier)

                
        else:
            # Si la guía no existe, hacemos los inserts
            new_guia = Guia.Guia(
                no_guia = kwargs.get("no_guia"),
                fecha = kwargs.get("Fecha_guia")
            )
            session.add(new_guia)
            
            new_remitente = Remitente.Remitente(
                No_guia = kwargs.get("no_guia"),
                compania = kwargs.get("REMITENTE_compania"),
                contacto = kwargs.get("REMITENTE_contacto"),
                email = kwargs.get("REMITENTE_email"),
                direccion = kwargs.get("REMITENTE_direccion"),
                codigo_postal = kwargs.get("REMITENTE_codigo_postal"),
                ciudad = kwargs.get("REMITENTE_ciudad"),
                estado = kwargs.get("REMITENTE_estado"),
                pais = kwargs.get("REMITENTE_pais"),
                telefono = kwargs.get("REMITENTE_telefono")
                
            )
            session.add(new_remitente)
            
            new_destino = Destino.Destino(
                No_guia = kwargs.get("no_guia"),
                nombre = kwargs.get("DESTINO_nombre"),
                direccion = kwargs.get("DESTINO_direccion"),
                codigo_postal = kwargs.get("DESTINO_codigo_postal"),
                ciudad = kwargs.get("DESTINO_ciudad"),
                estado = kwargs.get("DESTINO_estado"),
                pais = kwargs.get("DESTINO_pais"),
                telefono = kwargs.get("DESTINO_telefono")
            )
            session.add(new_destino)
            
            new_paquete = Paquete(
                No_guia = kwargs.get("no_guia"),
                contenido = kwargs.get("contenido"),
                piezas = kwargs.get("piezas"),
                peso_libras = kwargs.get("peso_libras"),
                peso_kilos = kwargs.get("peso_kilos"),
                valor_declarado = kwargs.get("valor_declarado"),
                news = kwargs.get("news"),
                linea_de_negocio = kwargs.get("linea_de_negocio"),
                pre_alerta = kwargs.get("pre_alerta"),
                guia_externa = kwargs.get("guia_externa"),
                precinto = kwargs.get("precinto"),
                largo = kwargs.get("largo"),
                alto = kwargs.get("alto"),
                ancho = kwargs.get("ancho"),
                carrier = kwargs.get("carrier")
            )
            session.add(new_paquete)
            
        session.commit()
        return True

    except Exception as e:
        return False

    finally:
        session.close()