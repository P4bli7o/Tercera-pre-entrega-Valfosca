from django import forms
from AppValfosca.models import Mayorista, Minorista, Pedido, Cancelacion

class MayoristaForm(forms.ModelForm):
    class Meta:
        model = Mayorista
        fields = '__all__'

class MinoristaForm(forms.ModelForm):
    class Meta:
        model = Minorista
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class CancelacionForm(forms.ModelForm):
    class Meta:
        model = Cancelacion
        fields = '__all__'

