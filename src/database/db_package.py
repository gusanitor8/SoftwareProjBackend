from config.database import Session
from dataModels.paquete import PaqueteBase
from models.paquete_table import Paquete
from models.consolidado_table import Consolidado
from models.consolidacion_table import Consolidacion
from datetime import date
from typing import List


def upload_packages(packages: List[PaqueteBase], consolidado_id: int, descripcion: str, fecha: date,
                    transportista: str):
    try:
        session = Session()

        consolidado = Consolidado(
            id_consolidado=consolidado_id,
            descripcion=descripcion,
            fecha_consolidacion=fecha,
            transportista=transportista
        )

        session.add(consolidado)

        for index, package in enumerate(packages):
            paquete = Paquete(
                id_paquete=package.id_paquete,
                factura=package.factura,
                fecha_orden=package.fecha_orden,
                contenido=package.contenido,
                descripcion=package.descripcion,
                alto=package.alto,
                ancho=package.ancho,
                largo=package.largo,
                peso_libras=package.peso_libras,
                peso_volumetrico=package.peso_volumetrico,
                valor_producto_dolar=package.valor_producto_dolar,
                unidades=package.unidades,
                direccion_casillero=package.direccion_casillero,
                empresa_remitente=package.empresa_remitente,
                cliente_nombre=package.cliente_nombre,
                cliente_telefono=package.cliente_telefono,
                cliente_email=package.cliente_email,
                cliente_direccion=package.cliente_direccion
            )

            session.add(paquete)
            packages[index] = paquete


        for paquete in packages:
            consolidacion = Consolidacion(
                consolidado_id=consolidado_id,
                paquete_id=paquete.id_paquete
            )

        session.commit()

    finally:
        session.close()
