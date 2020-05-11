from django import forms
from .models import CheckoutLine,Checkout


class AddToCheckout(forms.ModelForm):
    class Meta:
        model = CheckoutLine
        exclude = ('product', 'checkout')
