from AppValfosca.models import Mayorista, Minorista, Pedido, Cancelacion



Mayorista(nombre_de_empresa = "WorldTech",
          cuit = "5468352445",
          nombre = "Matias",
          apellido = "Palmero",
          fecha_de_nacimiento = "21-10-92",
          dni = "37561345",
          email = "info@worldtech.com",
          direccion = "Lavalle 925",
          telefono = "03416253251",
          codigo_postal = "2000",
        ).save()



Minorista(nombre = "Paula",
          apellido = "Arroyo",
          fecha_de_nacimiento = "10-12-85",
          dni = "32346824",
          email = "pau_arro@gmail.com",
          direccion = "Maipu 1021",
          telefono = "023523512356",
          codigo_postal = "3250"
        ).save()



Pedido(nombre_y_apellido_del_comprador = "Roberto Machado",
        producto_a_comprar = "Memoria ram ddr5 GsKill 16gb",
        cantidad = "4",
        metodo_de_pago= "Efectivo",
        retira_en_sucursal = "Si",
        quien_retira = "Roberto Machado",
        comentarios = "Voy a pasar por la tarde sobre el cierre, por favor tener los productos preparados"
        ).save()



Cancelacion(fecha_de_compra_factura = "09-03-23",
            nro_de_orden_de_compra  = "548236",
            nombre_y_apellido_del_comprador = "Esteban Miranda",
            sucursal_donde_realizo_la_compra = "Palermo",
            desea_cancelar_algun_pedido = "No",
            desea_realizar_algun_cambio = "Si",
            comentarios = "El producto vino con una falla y tiene signos de uso"
            ).save()
