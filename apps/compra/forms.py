from django.forms import ModelForm, Form

from django import forms

from apps.compra.models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cantidad']


class PagoForm(forms.Form):
    ping = forms.CharField(max_length=6)
    password = forms.CharField(max_length=50)
    numero_de_cuenta = forms.CharField(max_length=16)
