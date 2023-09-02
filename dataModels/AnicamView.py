from pydantic import BaseModel

class AnicamView(BaseModel):
    no_guia	: int
    fecha	: str
    REMITENTE_compania	: str
    REMITENTE_contacto	: str
    REMITENTE_email	: str
    REMITENTE_direccion	: str
    REMITENTE_codigo_postal	: str
    REMITENTE_ciudad	: str
    REMITENTE_estado	: str
    REMITENTE_pais	: str
    REMITENTE_telefono	: str
    DESTINO_nombre	: str
    DESTINO_direccion	: str
    DESTINO_codigo_postal: int
    DESTINO_ciudad: str
    DESTINO_codigo_postal: int
    DESTINO_direccion: str
    DESTINO_estado: str
    DESTINO_nombre: str
    DESTINO_pais: str
    DESTINO_telefono: int
    REMITENTE_ciudad: str
    REMITENTE_codigo_postal: int
    REMITENTE_compania: str
    REMITENTE_contacto: str
    REMITENTE_direccion: str
    REMITENTE_email: str
    REMITENTE_estado: str
    REMITENTE_pais: str
    REMITENTE_telefono: int
    alto: float
    ancho: float
    carrier: str
    contenido: str
    fecha: str
    guia_externa: int
    largo: float
    linea_de_negocio: str
    news: str
    no_guia: int
    peso_kilos: float
    peso_libras: float
    piezas: int
    pre_alerta: int
    precinto: str
    valor_declarado: int

    class Config:
        orm_mode = True