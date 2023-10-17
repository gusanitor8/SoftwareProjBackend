from config.database import Session
from sqlalchemy import text
from datetime import date
#from models import Cuscar, Guia, Remitente, Destino, Paquete, Oea, Costeo

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
    

def getAnicamView():
    pass
    # try:
    #     session = Session()
    #     view_query = text("SELECT * FROM anicam_table_view")
    #     result = session.execute(view_query)
    #
    #     # Fetch all data from the result
    #     rows = result.fetchall()
    #     column_names = result.keys()  # Extract column names
    #
    #     # Combine column names and rows into a list of dictionaries
    #     data = jsonifyResponse(rows, column_names)
    #
    #     return data
    # finally:
    #     session.close()


def getCuscarView():
    pass
    # try:
    #     session = Session()
    #     query = session.query(Cuscar.Cuscar).all()
    #     return query
    # finally:
    #     session.close()

def getAnicamViewSql():
    pass
    # session = Session()
    # query = session.query(
    #     #tabla guia
    #     Guia.Guia.no_guia,
    #     Guia.Guia.fecha,
    #
    #     #tabla remitente
    #     Remitente.Remitente.REMITENTE_compania,
    #     Remitente.Remitente.REMITENTE_contacto,
    #     Remitente.Remitente.REMITENTE_email,
    #     Remitente.Remitente.REMITENTE_direccion,
    #     Remitente.Remitente.REMITENTE_codigo_postal,
    #     Remitente.Remitente.REMITENTE_ciudad,
    #     Remitente.Remitente.REMITENTE_estado,
    #     Remitente.Remitente.REMITENTE_pais,
    #     Remitente.Remitente.REMITENTE_telefono,
    #
    #     #tabla destino
    #     Destino.Destino.DESTINO_nombre,
    #     Destino.Destino.DESTINO_direccion,
    #     Destino.Destino.DESTINO_codigo_postal,
    #     Destino.Destino.DESTINO_ciudad,
    #     Destino.Destino.DESTINO_estado,
    #     Destino.Destino.DESTINO_pais,
    #     Destino.Destino.DESTINO_telefono,
    #
    #     #tabla paquete
    #     Paquete.Paquete.contenido,
    #     Paquete.Paquete.piezas,
    #     Paquete.Paquete.peso_libras,
    #     Paquete.Paquete.peso_kilos,
    #     Paquete.Paquete.valor_declarado,
    #     Paquete.Paquete.news,
    #     Paquete.Paquete.linea_de_negocio,
    #     Paquete.Paquete.pre_alerta,
    #     Paquete.Paquete.guia_externa,
    #     Paquete.Paquete.precinto,
    #     Paquete.Paquete.largo,
    #     Paquete.Paquete.alto,
    #     Paquete.Paquete.ancho,
    #     Paquete.Paquete.carrier
    # ).join(Remitente.Remitente, Guia.Guia.no_guia == Remitente.Remitente.No_guia).\
    #     join(Destino.Destino, Guia.Guia.no_guia == Destino.Destino.No_guia).\
    #     join(Paquete.Paquete, Guia.Guia.no_guia == Paquete.Paquete.No_guia)
    #
    # rows = query.all()
    #
    # column_names = column_names = [desc['name'] for desc in query.column_descriptions]
    #
    # result = jsonifyResponse(rows, column_names)
    # return result


def updateAnicamData(**kwargs):
    pass
    # session = Session()
    #
    # try:
    #     # Verificamos si la guía existe
    #     guia_exists = session.query(Guia.Guia).filter(Guia.Guia.no_guia == kwargs.get("no_guia")).first()
    #
    #     # Si la guía existe, hacemos los updates
    #     if guia_exists:
    #
    #         # Actualizamos los datos de la guia
    #         session.query(Guia.Guia).filter(Guia.Guia.no_guia == kwargs.get("no_guia")).update({
    #             "fecha": kwargs.get("Fecha_guia")
    #         })
    #
    #
    #         # Actualizamos los datos del remitente
    #         remitente_values = {
    #             "REMITENTE_compania": kwargs.get("REMITENTE_compania"),
    #             "REMITENTE_contacto": kwargs.get("REMITENTE_contacto"),
    #             "REMITENTE_email": kwargs.get("REMITENTE_email"),
    #             "REMITENTE_direccion": kwargs.get("REMITENTE_direccion"),
    #             "REMITENTE_codigo_postal": kwargs.get("REMITENTE_codigo_postal"),
    #             "REMITENTE_ciudad": kwargs.get("REMITENTE_ciudad"),
    #             "REMITENTE_estado": kwargs.get("REMITENTE_estado"),
    #             "REMITENTE_pais": kwargs.get("REMITENTE_pais"),
    #             "REMITENTE_telefono": kwargs.get("REMITENTE_telefono")
    #         }
    #         session.query(Remitente.Remitente).filter(Remitente.Remitente.No_guia == kwargs.get("no_guia")).update(remitente_values)
    #
    #
    #         # Actualizamos los datos del destino
    #         destino_values = {
    #             "DESTINO_nombre": kwargs.get("DESTINO_nombre"),
    #             "DESTINO_direccion": kwargs.get("DESTINO_direccion"),
    #             "DESTINO_codigo_postal": kwargs.get("DESTINO_codigo_postal"),
    #             "DESTINO_ciudad": kwargs.get("DESTINO_ciudad"),
    #             "DESTINO_estado": kwargs.get("DESTINO_estado"),
    #             "DESTINO_pais": kwargs.get("DESTINO_pais"),
    #             "DESTINO_telefono": kwargs.get("DESTINO_telefono")
    #         }
    #         session.query(Destino.Destino).filter(Destino.Destino.No_guia == kwargs.get("no_guia")).update(destino_values)
    #
    #
    #         # Actualizamos los datos del paquete
    #         paquete_values = {
    #             "contenido": kwargs.get("contenido"),
    #             "piezas": kwargs.get("piezas"),
    #             "peso_libras": kwargs.get("peso_libras"),
    #             "peso_kilos": kwargs.get("peso_kilos"),
    #             "valor_declarado": kwargs.get("valor_declarado"),
    #             "news": kwargs.get("news"),
    #             "linea_de_negocio": kwargs.get("linea_de_negocio"),
    #             "pre_alerta": kwargs.get("pre_alerta"),
    #             "guia_externa": kwargs.get("guia_externa"),
    #             "precinto": kwargs.get("precinto"),
    #             "largo": kwargs.get("largo"),
    #             "alto": kwargs.get("alto"),
    #             "ancho": kwargs.get("ancho"),
    #             "carrier": kwargs.get("carrier")
    #         }
    #         session.query(Paquete.Paquete).filter(Paquete.Paquete.No_guia == kwargs.get("no_guia")).update(paquete_values)


        # # Si la guía no existe, hacemos los inserts
        # else:
        #
        #     # Creamos un nuevo resgistro para Guia
        #     new_guia = Guia.Guia(
        #         no_guia = kwargs.get("no_guia"),
        #         fecha = kwargs.get("Fecha_guia")
        #     )
        #     session.add(new_guia)
        #
        #
        #     # Creamos un nuevo registro para Remitente
        #     new_remitente = Remitente.Remitente(
        #         No_guia = kwargs.get("no_guia"),
        #         REMITENTE_compania = kwargs.get("REMITENTE_compania"),
        #         REMITENTE_contacto = kwargs.get("REMITENTE_contacto"),
        #         REMITENTE_email = kwargs.get("REMITENTE_email"),
        #         REMITENTE_direccion = kwargs.get("REMITENTE_direccion"),
        #         REMITENTE_codigo_postal = kwargs.get("REMITENTE_codigo_postal"),
        #         REMITENTE_ciudad = kwargs.get("REMITENTE_ciudad"),
        #         REMITENTE_estado = kwargs.get("REMITENTE_estado"),
        #         REMITENTE_pais = kwargs.get("REMITENTE_pais"),
        #         REMITENTE_telefono = kwargs.get("REMITENTE_telefono")
        #
        #     )
        #     session.add(new_remitente)
        #
        #
        #     # Creamos un nuevo registro para Destino
        #     new_destino = Destino.Destino(
        #         No_guia = kwargs.get("no_guia"),
        #         DESTINO_nombre = kwargs.get("DESTINO_nombre"),
        #         DESTINO_direccion = kwargs.get("DESTINO_direccion"),
        #         DESTINO_codigo_postal = kwargs.get("DESTINO_codigo_postal"),
        #         DESTINO_ciudad = kwargs.get("DESTINO_ciudad"),
        #         DESTINO_estado = kwargs.get("DESTINO_estado"),
        #         DESTINO_pais = kwargs.get("DESTINO_pais"),
        #         DESTINO_telefono = kwargs.get("DESTINO_telefono")
        #     )
        #     session.add(new_destino)
        #
        #
        #     # Creamos un nuevo registro para Paquete
        #     new_paquete = Paquete.Paquete(
        #         No_guia = kwargs.get("no_guia"),
        #         contenido = kwargs.get("contenido"),
        #         piezas = kwargs.get("piezas"),
        #         peso_libras = kwargs.get("peso_libras"),
        #         peso_kilos = kwargs.get("peso_kilos"),
        #         valor_declarado = kwargs.get("valor_declarado"),
        #         news = kwargs.get("news"),
        #         linea_de_negocio = kwargs.get("linea_de_negocio"),
        #         pre_alerta = kwargs.get("pre_alerta"),
        #         guia_externa = kwargs.get("guia_externa"),
        #         precinto = kwargs.get("precinto"),
        #         largo = kwargs.get("largo"),
        #         alto = kwargs.get("alto"),
        #         ancho = kwargs.get("ancho"),
        #         carrier = kwargs.get("carrier")
        #     )
        #     session.add(new_paquete)
        #
        #
        # # Guardamos los cambios hechos en la base de datos
        # session.commit()
        # return True



    # finally:
    #     session.close()
    #
    # return True

        

def getFinancesViewSql():
    pass
    # try:
    #     session = Session()
    #
    #     query = session.query(
    #         # Tabla Guia
    #         Guia.Guia.no_guia.label("No_guia"),
    #
    #         # Tabla Costeo
    #         Costeo.Costeo.codigo,
    #         Costeo.Costeo.courier,
    #         Costeo.Costeo.correlativo,
    #         Costeo.Costeo.consignatario,
    #         Costeo.Costeo.libras_a_facturar,
    #         Costeo.Costeo.peso_real_lb,
    #         Costeo.Costeo.peso_vol_lb,
    #         Costeo.Costeo.descripcion_costeo,
    #         Costeo.Costeo.cobro_flete,
    #         Costeo.Costeo.ultima_milla,
    #         Costeo.Costeo.gestion_aduana,
    #         Costeo.Costeo.manejo_almacenaje,
    #         Costeo.Costeo.descuentos,
    #         Costeo.Costeo.DAI,
    #         Costeo.Costeo.IVA,
    #
    #         # Tabla OEA
    #         Oea.OEA.Numero_de_Declaracion,
    #         Oea.OEA.Declaracion,
    #         Oea.OEA.Selectivo
    #     ).join(Costeo.Costeo, Guia.Guia.no_guia == Costeo.Costeo.No_guia).\
    #         join(Oea.OEA, Guia.Guia.no_guia == Oea.OEA.No_guia)
    #
    #     rows = query.all()
    #
    #     column_names = [desc['name'] for desc in query.column_descriptions]
    #
    #     result = jsonifyResponse(rows, column_names)
    #     return result
    #
    # finally:
    #     session.close()


def updateFinancesData(**kwargs):
    # session = Session()
    #
    # try:
    #     # Verificamos si la guía existe
    #     oea_exist = session.query(Oea.OEA).filter(Oea.OEA.Numero_de_Declaracion == kwargs.get("Numero_de_Declaracion")).first()
    #     guia_exists = session.query(Guia.Guia).filter(Guia.Guia.no_guia == kwargs.get("No_guia")).first()
    #
    #     # Si la guía existe, hacemos los updates
    #     if oea_exist:
    #         if guia_exists:
    #             # Actualizamos los datos de Costeo
    #             costeo_values = {
    #                 "codigo": kwargs.get("codigo"),
    #                 "courier": kwargs.get("courier"),
    #                 "correlativo": kwargs.get("correlativo"),
    #                 "consignatario": kwargs.get("consignatario"),
    #                 "libras_a_facturar": kwargs.get("libras_a_facturar"),
    #                 "peso_real_lb": kwargs.get("peso_real_lb"),
    #                 "peso_vol_lb": kwargs.get("peso_vol_lb"),
    #                 "descripcion_costeo": kwargs.get("descripcion_costeo"),
    #                 "cobro_flete": kwargs.get("cobro_flete"),
    #                 "ultima_milla": kwargs.get("ultima_milla"),
    #                 "gestion_aduana": kwargs.get("gestion_aduana"),
    #                 "manejo_almacenaje": kwargs.get("manejo_almacenaje"),
    #                 "descuentos": kwargs.get("descuentos"),
    #                 "DAI": kwargs.get("DAI"),
    #                 "IVA": kwargs.get("IVA")
    #             }
    #             session.query(Costeo.Costeo).filter(Costeo.Costeo.No_guia == kwargs.get("No_guia")).update(costeo_values)
    #
    #             # Actualizamos los datos de OEA
    #             oea_values = {
    #                 "Numero_de_Declaracion": kwargs.get("Numero_de_Declaracion"),
    #                 "Declaracion": kwargs.get("Declaracion"),
    #                 "Selectivo": kwargs.get("Selectivo")
    #             }
    #             session.query(Oea.OEA).filter(Oea.OEA.No_guia == kwargs.get("No_guia")).update(oea_values)
    #
    #         else:
    #             pass # Aqui en este punto deberia de suceder algo en caso se quiera hacer un update para una guia que no existe pero la OEA si existe
    #
    #     # Si la OEA no existe
    #     else:
    #         # pero la guia si existe hacer los inserts nuevos
    #         if guia_exists:
    #
    #             # Creamos un nuevo registro para Costeo
    #             new_costeo = Costeo.Costeo(
    #                 No_guia = kwargs.get("No_guia"),
    #                 codigo = kwargs.get("codigo"),
    #                 courier = kwargs.get("courier"),
    #                 correlativo = kwargs.get("correlativo"),
    #                 consignatario = kwargs.get("consignatario"),
    #                 libras_a_facturar = kwargs.get("libras_a_facturar"),
    #                 peso_real_lb = kwargs.get("peso_real_lb"),
    #                 peso_vol_lb = kwargs.get("peso_vol_lb"),
    #                 descripcion_costeo = kwargs.get("descripcion_costeo"),
    #                 cobro_flete = kwargs.get("cobro_flete"),
    #                 ultima_milla = kwargs.get("ultima_milla"),
    #                 gestion_aduana = kwargs.get("gestion_aduana"),
    #                 manejo_almacenaje = kwargs.get("manejo_almacenaje"),
    #                 descuentos = kwargs.get("descuentos"),
    #                 DAI = kwargs.get("DAI"),
    #                 IVA = kwargs.get("IVA")
    #             )
    #             session.add(new_costeo)
    #
    #             # Creamos un nuevo registro para OEA
    #             new_oea = Oea.OEA(
    #                 No_guia = kwargs.get("No_guia"),
    #                 Numero_de_Declaracion = kwargs.get("Numero_de_Declaracion"),
    #                 Declaracion = kwargs.get("Declaracion"),
    #                 Selectivo = kwargs.get("Selectivo")
    #             )
    #             session.add(new_oea)
    #
    #         # si ni la guia ni la OEA existen, entonces crear los nuevos registros para todo
    #         else:
    #             # Obtener la fecha actual en el formato dd-mm-yyyy
    #             fecha_actual = date.today().strftime("%d/%m/%Y")
    #
    #              # Creamos un nuevo resgistro para Guia
    #             new_guia = Guia.Guia(
    #                 no_guia = kwargs.get("No_guia"),
    #                 fecha = fecha_actual
    #             )
    #             session.add(new_guia)
    #
    #             # Creamos un nuevo registro para Costeo
    #             new_costeo = Costeo.Costeo(
    #                 No_guia = kwargs.get("No_guia"),
    #                 codigo = kwargs.get("codigo"),
    #                 courier = kwargs.get("courier"),
    #                 correlativo = kwargs.get("correlativo"),
    #                 consignatario = kwargs.get("consignatario"),
    #                 libras_a_facturar = kwargs.get("libras_a_facturar"),
    #                 peso_real_lb = kwargs.get("peso_real_lb"),
    #                 peso_vol_lb = kwargs.get("peso_vol_lb"),
    #                 descripcion_costeo = kwargs.get("descripcion_costeo"),
    #                 cobro_flete = kwargs.get("cobro_flete"),
    #                 ultima_milla = kwargs.get("ultima_milla"),
    #                 gestion_aduana = kwargs.get("gestion_aduana"),
    #                 manejo_almacenaje = kwargs.get("manejo_almacenaje"),
    #                 descuentos = kwargs.get("descuentos"),
    #                 DAI = kwargs.get("DAI"),
    #                 IVA = kwargs.get("IVA")
    #             )
    #             session.add(new_costeo)
    #
    #             # Creamos un nuevo registro para OEA
    #             new_oea = Oea.OEA(
    #                 No_guia = kwargs.get("No_guia"),
    #                 Numero_de_Declaracion = kwargs.get("Numero_de_Declaracion"),
    #                 Declaracion = kwargs.get("Declaracion"),
    #                 Selectivo = kwargs.get("Selectivo")
    #             )
    #             session.add(new_oea)
    #
    #
    #     session.commit()
    #     return True

    # finally:
    #     session.close()
    pass