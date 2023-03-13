from django.contrib import admin
from AppValfosca.models import Mayorista, Minorista, Pedido, Cancelacion
admin.site.register(Mayorista)
admin.site.register(Minorista)
admin.site.register(Pedido)
admin.site.register(Cancelacion)

