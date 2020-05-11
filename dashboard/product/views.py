from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.http import require_POST
from django.views.generic import CreateView,UpdateView,ListView
from product.models import Product,ProductImage

from dashboard.product.forms import ProdutImageForm


class CreateProduct(CreateView):
    model = Product
    template_name = "dashboard/product/create.html"
    fields = ['name', 'description', "price", "weight",
              "sku", "stock", "brand", "category"]

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(CreateProduct, self).form_valid(form)


class UpdateProduct(UpdateView):
    model = Product
    template_name = "dashboard/product/create.html"
    fields = ['name', 'description', "price", "weight",
              "sku", "stock", "brand", "category"]

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(UpdateProduct, self).form_valid(form)


class ListProduct(ListView):
    model = Product
    template_name = "dashboard/product/list.html"


class ListImages(ListView):
    model = ProductImage
    template_name = 'dashboard/product/image_form.html'

    def get_queryset(self):
        return super(ListImages, self).get_queryset().filter(product__id=self.kwargs.get('pk'))


def create_image(request, pk):
    product = get_object_or_404(Product, id=pk)
    print(request.FILES)
    print(request.POST)
    form = ProdutImageForm(request.POST, request.FILES, product=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('dashboard:product_dashboard:product_list'))
    print(form.errors)
    return HttpResponseRedirect(reverse('dashboard:product_dashboard:product_list'))
