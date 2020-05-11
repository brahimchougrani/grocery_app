from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView,DetailView

from .models import Product, Category, ProductImage
from datetime import timedelta
from django.http import JsonResponse
from checkout.form import AddToCheckout
from checkout.models import Checkout, CheckoutLine
from product.models import Product


class DetailProduct(DetailView):
    model = Product
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailProduct, self).get_context_data(**kwargs)
        context['checkout_form'] = AddToCheckout()
        return context


class ListProduct(ListView):
    model = Product
    template_name = 'product/list.html'
    paginate_by = 1

    def get_queryset(self):
        category = get_object_or_404(Category,slug=self.kwargs.get('slug'))
        categories = category.get_descendants(include_self=True)
        qs = super(ListProduct, self).get_queryset().filter(
            category__in=categories
        )
        return qs








def set_checkout_cookie(simple_checkout, response):
    """Update response with a checkout token cookie."""
    # FIXME: document why session is not used
    max_age = int(timedelta(days=30).total_seconds())
    response.set_signed_cookie('checkout', simple_checkout.token, max_age=max_age)


def get_or_create_checkout_from_request(
    request, checkout_queryset=Checkout.objects.all()):
    if request.user.is_authenticated:
        return checkout_queryset.get_or_create(
            user=request.user,email=request.user.email
        )[0]
    token = request.get_signed_cookie('checkout', default=None)
    return checkout_queryset.filter(token=token, user=None).get_or_create(
        user=None
    )[0]


def product_add_to_checkout(request, slug):
        checkout = get_or_create_checkout_from_request(request)
        product = Product.objects.get(slug=slug)
        instance = CheckoutLine(product=product, checkout=checkout)
        form = AddToCheckout(request.POST, instance=instance)
        if form.is_valid() and product.in_stock(int(request.POST.get('quantity'))):
            checkout_line = CheckoutLine.objects.filter(checkout=checkout,
                        product=product)
            if checkout_line.exists():
                instance = checkout_line[0]
                instance.quantity += int(request.POST.get('quantity'))
                instance.save()
            else:
                form.save()
            if request.is_ajax():
                response = JsonResponse({"next": reverse("checkout:index")}, status=200)
            else:
                response = redirect("dashboard:product_dashboard:product_list")
        else:
            if request.is_ajax():
                response = JsonResponse({"error": form.errors}, status=400)
            else:
                response = redirect(reverse('products:detail_product',kwargs={
                    'slug': product.slug
                }))
        if not request.user.is_authenticated:
            set_checkout_cookie(checkout, response)
        return response

