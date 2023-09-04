from config.database import Session
from sqlalchemy import text
from datetime import date
from models import Cuscar, Guia, Remitente, Destino, Paquete, Oea, Costeo


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
        query = session.query(Cuscar.Cuscar).all()
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
        Remitente.Remitente.REMITENTE_compania,
        Remitente.Remitente.REMITENTE_contacto,
        Remitente.Remitente.REMITENTE_email,
        Remitente.Remitente.REMITENTE_direccion,
        Remitente.Remitente.REMITENTE_codigo_postal,
        Remitente.Remitente.REMITENTE_ciudad,
        Remitente.Remitente.REMITENTE_estado,
        Remitente.Remitente.REMITENTE_pais,
        Remitente.Remitente.REMITENTE_telefono,

        #tabla destino
        Destino.Destino.DESTINO_nombre,
        Destino.Destino.DESTINO_direccion,
        Destino.Destino.DESTINO_codigo_postal,
        Destino.Destino.DESTINO_ciudad,
        Destino.Destino.DESTINO_estado,
        Destino.Destino.DESTINO_pais,
        Destino.Destino.DESTINO_telefono,

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
        guia_exists = session.query(Guia.Guia).filter(Guia.Guia.no_guia == kwargs.get("no_guia")).first()
        
        # Si la guía existe, hacemos los updates
        if guia_exists:

            # Actualizamos los datos de la guia
            session.query(Guia.Guia).filter(Guia.Guia.no_guia == kwargs.get("no_guia")).update({
                "fecha": kwargs.get("Fecha_guia")
            })


            # Actualizamos los datos del remitente
            remitente_values = {
                "REMITENTE_compania": kwargs.get("REMITENTE_compania"),
                "REMITENTE_contacto": kwargs.get("REMITENTE_contacto"),
                "REMITENTE_email": kwargs.get("REMITENTE_email"),
                "REMITENTE_direccion": kwargs.get("REMITENTE_direccion"),
                "REMITENTE_codigo_postal": kwargs.get("REMITENTE_codigo_postal"),
                "REMITENTE_ciudad": kwargs.get("REMITENTE_ciudad"),
                "REMITENTE_estado": kwargs.get("REMITENTE_estado"),
                "REMITENTE_pais": kwargs.get("REMITENTE_pais"),
                "REMITENTE_telefono": kwargs.get("REMITENTE_telefono")
            }
            session.query(Remitente.Remitente).filter(Remitente.Remitente.No_guia == kwargs.get("no_guia")).update(remitente_values)


            # Actualizamos los datos del destino
            destino_values = {
                "DESTINO_nombre": kwargs.get("DESTINO_nombre"),
                "DESTINO_direccion": kwargs.get("DESTINO_direccion"),
                "DESTINO_codigo_postal": kwargs.get("DESTINO_codigo_postal"),
                "DESTINO_ciudad": kwargs.get("DESTINO_ciudad"),
                "DESTINO_estado": kwargs.get("DESTINO_estado"),
                "DESTINO_pais": kwargs.get("DESTINO_pais"),
                "DESTINO_telefono": kwargs.get("DESTINO_telefono")
            }
            session.query(Destino.Destino).filter(Destino.Destino.No_guia == kwargs.get("no_guia")).update(destino_values)


            # Actualizamos los datos del paquete
            paquete_values = {
                "contenido": kwargs.get("contenido"),
                "piezas": kwargs.get("piezas"),
                "peso_libras": kwargs.get("peso_libras"),
                "peso_kilos": kwargs.get("peso_kilos"),
                "valor_declarado": kwargs.get("valor_declarado"),
                "news": kwargs.get("news"),
                "linea_de_negocio": kwargs.get("linea_de_negocio"),
                "pre_alerta": kwargs.get("pre_alerta"),
                "guia_externa": kwargs.get("guia_externa"),
                "precinto": kwargs.get("precinto"),
                "largo": kwargs.get("largo"),
                "alto": kwargs.get("alto"),
                "ancho": kwargs.get("ancho"),
                "carrier": kwargs.get("carrier")
            }
            session.query(Paquete.Paquete).filter(Paquete.Paquete.No_guia == kwargs.get("no_guia")).update(paquete_values)


        # Si la guía no existe, hacemos los inserts   
        else:
            
            # Creamos un nuevo resgistro para Guia
            new_guia = Guia.Guia(
                no_guia = kwargs.get("no_guia"),
                fecha = kwargs.get("Fecha_guia")
            )
            session.add(new_guia)
            

            # Creamos un nuevo registro para Remitente
            new_remitente = Remitente.Remitente(
                No_guia = kwargs.get("no_guia"),
                REMITENTE_compania = kwargs.get("REMITENTE_compania"),
                REMITENTE_contacto = kwargs.get("REMITENTE_contacto"),
                REMITENTE_email = kwargs.get("REMITENTE_email"),
                REMITENTE_direccion = kwargs.get("REMITENTE_direccion"),
                REMITENTE_codigo_postal = kwargs.get("REMITENTE_codigo_postal"),
                REMITENTE_ciudad = kwargs.get("REMITENTE_ciudad"),
                REMITENTE_estado = kwargs.get("REMITENTE_estado"),
                REMITENTE_pais = kwargs.get("REMITENTE_pais"),
                REMITENTE_telefono = kwargs.get("REMITENTE_telefono")
                
            )
            session.add(new_remitente)
            

            # Creamos un nuevo registro para Destino
            new_destino = Destino.Destino(
                No_guia = kwargs.get("no_guia"),
                DESTINO_nombre = kwargs.get("DESTINO_nombre"),
                DESTINO_direccion = kwargs.get("DESTINO_direccion"),
                DESTINO_codigo_postal = kwargs.get("DESTINO_codigo_postal"),
                DESTINO_ciudad = kwargs.get("DESTINO_ciudad"),
                DESTINO_estado = kwargs.get("DESTINO_estado"),
                DESTINO_pais = kwargs.get("DESTINO_pais"),
                DESTINO_telefono = kwargs.get("DESTINO_telefono")
            )
            session.add(new_destino)
            

            # Creamos un nuevo registro para Paquete
            new_paquete = Paquete.Paquete(
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
            

        # Guardamos los cambios hechos en la base de datos
        session.commit()
        return True


    finally:
        session.close()
        

def getFinancesViewSql():
    try:
        session = Session()
        query = session.query(
            # Tabla Guia
            Guia.Guia.no_guia.label("No_guia"),

            # Tabla Costeo
            Costeo.Costeo.codigo,
            Costeo.Costeo.courier,
            Costeo.Costeo.correlativo,
            Costeo.Costeo.consignatario,
            Costeo.Costeo.libras_a_facturar,
            Costeo.Costeo.peso_real_lb,
            Costeo.Costeo.peso_vol_lb,
            Costeo.Costeo.descripcion_costeo,
            Costeo.Costeo.cobro_flete,
            Costeo.Costeo.ultima_milla,
            Costeo.Costeo.gestion_aduana,
            Costeo.Costeo.manejo_almacenaje,
            Costeo.Costeo.descuentos,
            Costeo.Costeo.DAI,
            Costeo.Costeo.IVA,

            # Tabla OEA
            Oea.OEA.Numero_de_Declaracion,
            Oea.OEA.Declaracion,
            Oea.OEA.Selectivo
        ).join(Costeo.Costeo, Guia.Guia.no_guia == Costeo.Costeo.No_guia).\
            join(Oea.OEA, Guia.Guia.no_guia == Oea.OEA.No_guia)
        
        rows = query.all()

        column_names = [desc['name'] for desc in query.column_descriptions]

        result = jsonifyResponse(rows, column_names)
        return result
    
    finally:
        session.close()
        
    return True