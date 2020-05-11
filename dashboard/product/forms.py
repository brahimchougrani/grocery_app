from django import forms

from product.models import ProductImage


class ProdutImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        exclude = ('product',)

    def __init__(self, *args, **kwargs):
        product = kwargs.pop("product")
        super().__init__(*args, **kwargs)
        self.instance.product = product
