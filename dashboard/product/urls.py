from django.urls import path
from . import views
from dashboard.decorators import user_dashboard_permession
app_name = 'product_dashboard'

urlpatterns = [
    path('create/',user_dashboard_permession(views.CreateProduct.as_view()),
         name='product_create'),
    path('update/<int:pk>/',user_dashboard_permession(views.UpdateProduct.as_view()),
         name='product_update'),
    path('list/',user_dashboard_permession(views.ListProduct.as_view()),
         name='product_list'),
    path('<int:pk>/images/', user_dashboard_permession(views.ListImages.as_view()),
         name='product_images'),
    path('<int:pk>/images/create', user_dashboard_permession(views.create_image),
         name='product_images_create'),
]
