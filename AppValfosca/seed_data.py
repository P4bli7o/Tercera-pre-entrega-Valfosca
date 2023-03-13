from AppValfosca.models import Mayorista, Minorista, Pedido, Cancelacion

Mayorista(nombre_empresa = "WorldTech",
          cuit = "5468352445",
          nombre = "Matias",
          apellido = "Palmero",
          fecha_nacimiento = "21-10-92",
          dni = "37561345",
          email = "info@worldtech.com",
          direccion = "Lavalle 925",
          telefono = "03416253251",
          c_postal = "2000"
        ).save()


Minorista(nombre = "Paula",
          apellido = "Arroyo",
          fecha_nacimiento = "10-12-85",
          dni = "32346824",
          email = "pau_arro@gmail.com",
          direccion = "Maipu 1021",
          telefono = "023523512356",
          c_postal = "3250"
        ).save()


Pedido(nombre = "Roberto",
        nombre_comprador  = "Machado",
        producto = "Memoria ram ddr5 GsKill 16gb",
        cantidad = "4",
        metodo_pago = "Efectivo",
        retiro = "En sucursal",
        quien_retira = "Roberto Machado",
        comentarios = "Voy a pasar por la tarde sobreel cierre, por favor tenerlo los productos preparados"
        ).save()



Cancelacion(fecha_factura = "09-03-23",
            nro_orden_compra  = "548236",
            nombre_comprador = "Esteban Miranda",
            sucursal = "Palermo",
            cancelar_pedido = "No",
            cambio = "Si",
            comentarios = "El producto vino con una falla y tiene signos de uso"
            ).save()

