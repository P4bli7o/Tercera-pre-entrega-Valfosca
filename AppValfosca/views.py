from django.shortcuts import render
from AppValfosca.models import Mayorista, Minorista, Pedido, Cancelacion
from AppValfosca.forms import MayoristaForm, MinoristaForm, PedidoForm, CancelacionForm

def index(request):
    return render(request, "AppValfosca/index.html")



def venta_mayorista(request):

    context = {
        "form": MayoristaForm(),
        "mayoristas": Mayorista.objects.all(),
    }
    return render(request, "AppValfosca/cte_mayorista.html", context)


def registrar_mayoristas(request):
    mayor_form = MayoristaForm(request.POST)
    mayor_form.save()
    context = {
        "form": MayoristaForm(),
        "mayoristas": Mayorista.objects.all(),

    }
    return render(request, "AppValfosca/cte_mayorista.html", context)





def venta_minorista(request):
    context = {
        "form" : MinoristaForm(),
        "minoristas": Minorista.objects.all(), 
    }
    return render(request, "AppValfosca/cte_minorista.html", context)


def registrar_minorista(request):
    minor_form = MinoristaForm(request.POST)
    minor_form.save()
    context = {
        "form": MinoristaForm(),
        "minoristas": Minorista.objects.all(),
    }
    return render(request, "AppValfosca/cte_minorista.html", context)




def pedidos(request):
    context = {
        "form": PedidoForm(),
        "pedidos": Pedido.objects.all(),
    }
    return render(request, "AppValfosca/pedidos.html", context)


def registrar_pedidos(request):
    pedido_form = PedidoForm(request.POST)
    pedido_form.save()
    context = {
        "form": PedidoForm(),
        "pedidos": Pedido.objects.all(),
    }
    return render(request, "AppValfosca/pedidos.html", context)



def cancelacion_pedidos(request):
    context = {
        "form": CancelacionForm(),
        "cancelaciones": Cancelacion.objects.all(),
    }
    return render(request, "AppValfosca/cancelaciones.html", context)


def registrar_cancelaciones(request):
    cancelar_form = CancelacionForm(request.POST)
    cancelar_form.save()
    context = {
        "form": CancelacionForm(),
        "cancelaciones": Cancelacion.objects.all()
    }
    return render(request, "AppValfosca/cancelaciones.html", context)





def buscar(request):
    criterio = request.GET.get("criterio", "")
    context = {
        "mayoristas": Mayorista.objects.filter(nombre__icontains = criterio).all(),
        "cp": Mayorista.objects.filter(codigo_postal__icontains = criterio).all(),
        "criterio_valido": criterio,
        "minoristas": Minorista.objects.filter(nombre__icontains = criterio).all(),
        "pedidos": Pedido.objects.filter(nombre_y_apellido_del_comprador__icontains = criterio).all(),
        "cancelaciones": Cancelacion.objects.filter(nombre_y_apellido_del_comprador__icontains = criterio).all(),
    }
    return render(request, "AppValfosca/buscar-todos.html", context)










