from django.urls import path
from .views import DetailProduct,ListProduct,product_add_to_checkout
app_name = "products"
urlpatterns = [
    path('<str:slug>/', DetailProduct.as_view(), name="detail_product"),
    path('category/<str:slug>/', ListProduct.as_view(), name="list_product"),
    path('add/<str:slug>/', product_add_to_checkout, name="add_to_checkout"),
]