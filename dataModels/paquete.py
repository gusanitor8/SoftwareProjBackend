from pydantic import BaseModel, constr, confloat, conint
from datetime import date

class PaqueteBase(BaseModel):
    # id_paquete autogenerado
    factura: constr(strip_whitespace=True, min_length=1)
    fecha_orden: date
    contenido: constr(strip_whitespace=True, min_length=1)
    descripcion: constr(strip_whitespace=True, min_length=1)
    alto: confloat(gt=0)
    ancho: confloat(gt=0)
    largo: confloat(gt=0)
    peso_libras: confloat(gt=0)
    peso_volumetrico: confloat(gt=0)
    valor_producto_dolar: confloat(gt=0)
    unidades: conint(ge=1)
    direccion_casillero: constr(strip_whitespace=True, min_length=1)
    empresa_remitente: constr(strip_whitespace=True, min_length=1)
    cliente_nombre: constr(strip_whitespace=True, min_length=1)
    cliente_telefono: constr(strip_whitespace=True, min_length=1)
    cliente_email: constr(strip_whitespace=True, pattern="^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$")
    cliente_direccion: constr(strip_whitespace=True, min_length=1)

    class Config:
        from_attributes = True
