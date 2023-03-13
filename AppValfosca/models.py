from django.db import models

class Mayorista(models.Model):
    nombre_empresa = models.CharField(max_length = 50)
    cuit = models.CharField(max_length = 11)
    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 40)
    fecha_nacimiento = models.CharField(max_length = 10)
    dni = models.CharField(max_length = 8)
    email = models.CharField(max_length = 40)
    direccion = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 20)
    c_postal = models.CharField(max_length = 10)

    def __str__(self):
        return f"""--Datos Cliente Mayorista--
    Nombre de la Empresa: {self.nombre_empresa}
    CUIT: {self.cuit}
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    Fecha de Nacimiento: {self.fecha_nacimiento}
    DNI: {self.dni}
    Correo electronico: {self.email}
    Direccion: {self.direccion}
    Telefono: {self.telefono}
    Codigo Postal: {self.c_postal}
    """


#Para probar si funciona la clase 
#py manage.py shell
#from AppValfosca.models import Mayorista    
#mayor = Mayorista("1","Pab","Val","123","p@.com","lalala 123","4513636453","2000")

class Minorista(models.Model):
    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 40)
    fecha_nacimiento = models.CharField(max_length = 10)
    dni = models.CharField(max_length = 8)
    email = models.CharField(max_length = 40)
    direccion = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 20)
    c_postal = models.CharField(max_length = 10)

    def __str__(self):
        return f"""--Datos Cliente Minorista--
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    Fecha de Nacimiento: {self.fecha_nacimiento}
    DNI: {self.dni}
    Correo electronico: {self.email}
    Direccion: {self.direccion}
    Telefono: {self.telefono}
    Codigo Postal: {self.c_postal}
    """


class Pedido(models.Model):
    nombre_comprador = models.CharField(max_length = 60)
    producto = models.CharField(max_length = 120)
    cantidad = models.CharField(max_length = 3)
    metodo_pago = models.CharField(max_length = 30)
    retiro = models.CharField(max_length = 4)
    quien_retira = models.CharField(max_length = 60)
    comentarios = models.CharField(max_length = 500)


    def __str__(self):
        return f"""--Datos de Pedidos--
    Nombre y Apellido del Comprador {self.nombre_comprador}
    Producto a comprar: {self.producto}
    Cantidad: {self.cantidad}
    Metodo de Pago: {self.metodo_pago}
    Retira en sucursal: {self.retiro}
    Quien Retira: {self.quien_retira}
    Comentario: {self.comentarios}
    """



class Cancelacion(models.Model):
    fecha_factura = models.CharField(max_length = 10)
    nro_orden_compra = models.CharField(max_length = 10)
    nombre_comprador = models.CharField(max_length = 60)
    sucursal = models.CharField(max_length = 50)
    cancelar_pedido = models.CharField(max_length = 100)
    cambio = models.CharField(max_length = 100)
    comentarios = models.CharField(max_length = 500)


    def __str__(self):
        return f"""--Datos de Cancelacion--
    Fecha de compra Factura: {self.fecha_factura}
    Nro de orden de compra: {self.nro_orden_compra}
    Nombre y Apellido del Comprador: {self.nombre_comprador}
    Sucursal donde realizo la compra: {self.sucursal}
    Desea cancelar el Pedido: {self.cancelar_pedido}
    Desea realizar algun cambio: {self.cambio}
    Comentario: {self.comentarios}
    """

