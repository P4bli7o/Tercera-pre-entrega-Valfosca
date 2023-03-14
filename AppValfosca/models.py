from django.db import models

class Mayorista(models.Model):
    nombre_de_empresa = models.CharField(max_length = 50)
    cuit = models.CharField(max_length = 11)
    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 40)
    fecha_de_nacimiento = models.CharField(max_length = 10)
    dni = models.CharField(max_length = 8)
    email = models.CharField(max_length = 40)
    direccion = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 20)
    codigo_postal = models.CharField(max_length = 10)

    def datos_mayoristas(self):
        return f"""--Datos Cliente Mayorista--
    Nombre de la Empresa: {self.nombre_de_empresa}
    CUIT: {self.cuit}
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    Fecha de Nacimiento: {self.fecha_de_nacimiento}
    DNI: {self.dni}
    Correo electronico: {self.email}
    Direccion: {self.direccion}
    Telefono: {self.telefono}
    Codigo Postal: {self.codigo_postal}
    """

    def __str__(self):
        return f"{self.nombre_de_empresa} - {self.direccion} - CP: {self.codigo_postal}"

#Para probar si funciona la clase 
#py manage.py shell
#from AppValfosca.models import Mayorista    
#mayor = Mayorista("1","Pab","Val","123","p@.com","lalala 123","4513636453","2000")

class Minorista(models.Model):
    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 40)
    fecha_de_nacimiento = models.CharField(max_length = 10)
    dni = models.CharField(max_length = 8)
    email = models.CharField(max_length = 40)
    direccion = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 20)
    codigo_postal = models.CharField(max_length = 10)

    def datos_minoristas(self):
        return f"""--Datos Cliente Minorista--
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    Fecha de Nacimiento: {self.fecha_de_nacimiento}
    DNI: {self.dni}
    Correo electronico: {self.email}
    Direccion: {self.direccion}
    Telefono: {self.telefono}
    Codigo Postal: {self.codigo_postal}
    """

    def __str__(self):
        return f"{self.apellido} - {self.nombre} - Email: {self.email}"
    




class Pedido(models.Model):
    nombre_y_apellido_del_comprador = models.CharField(max_length = 60)
    producto_a_comprar = models.CharField(max_length = 120)
    cantidad = models.CharField(max_length = 3)
    metodo_de_pago = models.CharField(max_length = 30)
    retira_en_sucursal = models.CharField(max_length = 4)
    quien_retira = models.CharField(max_length = 60)
    comentarios = models.CharField(max_length = 500)


    def datos_pedidos(self):
        return f"""--Datos de Pedidos--
    Nombre y Apellido del Comprador {self.nombre_y_apellido_del_comprador}
    Producto a comprar: {self.producto_a_comprar}
    Cantidad: {self.cantidad}
    Metodo de Pago: {self.metodo_de_pago}
    Retira en sucursal: {self.retira_en_sucursal}
    Quien Retira: {self.quien_retira}
    Comentario: {self.comentarios}
    """

    def __str__(self):
        return f"{self.nombre_y_apellido_del_comprador} - {self.producto_a_comprar} - Forma de pago: {self.metodo_de_pago}"





class Cancelacion(models.Model):
    fecha_de_compra_factura = models.CharField(max_length = 10)
    nro_de_orden_de_compra = models.CharField(max_length = 10)
    nombre_y_apellido_del_comprador = models.CharField(max_length = 60)
    sucursal_donde_realizo_la_compra = models.CharField(max_length = 50)
    desea_cancelar_algun_pedido = models.CharField(max_length = 100)
    desea_realizar_algun_cambio = models.CharField(max_length = 100)
    comentarios = models.CharField(max_length = 500)


    def datos_cancelacion(self):
        return f"""--Datos de Cancelacion--
    Fecha de compra Factura: {self.fecha_de_compra_factura}
    Nro de orden de compra: {self.nro_de_orden_de_compra}
    Nombre y Apellido del Comprador: {self.nombre_y_apellido_del_comprador}
    Sucursal donde realizo la compra: {self.sucursal_donde_realizo_la_compra}
    Desea cancelar el Pedido: {self.desea_cancelar_algun_pedido}
    Desea realizar algun cambio: {self.desea_realizar_algun_cambio}
    Comentario: {self.comentarios}
    """

    def __str__(self):
        return f"{self.nro_de_orden_de_compra} - {self.fecha_de_compra_factura} - Sucursal: {self.sucursal_donde_realizo_la_compra} - Cliente: {self.nombre_y_apellido_del_comprador}"
