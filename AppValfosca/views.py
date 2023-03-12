from django.shortcuts import render

def index(request):
    return render(request, "AppValfosca/index.html")

def venta_mayorista(request):
    return render(request, "AppValfosca/cte_mayorista.html")

def venta_minorista(request):
    return render(request, "AppValfosca/cte_minorista.html")

def pedidos(request):
    return render(request, "AppValfosca/pedidos.html")

def cancelacion_pedidos(request):
    return render(request, "AppValfosca/cancelaciones.html")

def buscar(request):
    return render(request, "AppValfosca/buscar.html")
