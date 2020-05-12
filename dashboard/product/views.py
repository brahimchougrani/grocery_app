from django.http import JsonResponse
from django.utils.text import slugify
from django.views.generic import CreateView,UpdateView,ListView
from product.models import Product,ProductImage
from django.shortcuts import get_object_or_404
from .forms import ProductImageForm


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


class ProductImageList(ListView):
    model = ProductImage
    template_name = 'dashboard/product/list_images.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductImageList, self).get_context_data(**kwargs)
        context['form'] = ProductImageForm()
        context['product_id'] = self.kwargs.get('pk')
        return context

    def get_queryset(self):
        return super(ProductImageList, self).get_queryset().filter(product__id=self.kwargs.get('pk'))


def create_image(request,pk):
    product = get_object_or_404(Product,pk=pk)
    form = ProductImageForm(request.POST,request.FILES)
    print(request.POST)
    print(request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.product = product
        obj.alt = product.name
        obj.save()
        return JsonResponse({'message': 'product image succesfuly created'}, status=200)
    print(form.errors)
    return JsonResponse({'message': form.errors}, status=400)