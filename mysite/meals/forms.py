from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


# class AddOrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ('worker', 'delivery')
#         widgets = {
#             'worker': forms.Select(attrs={'class': 'form-select'}),
#             'delivery': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
#         }


class AddMenuForm(forms.ModelForm):
    class Meta:
        model = ProductInOrder
        fields = ('order', 'product', 'num')
        widgets = {

        }


class AddProductInBasket(forms.Form):
    num = forms.IntegerField()


class AddOrderForm(forms.Form):
    worker = forms.ModelChoiceField(queryset=Worker.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    delivery = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))