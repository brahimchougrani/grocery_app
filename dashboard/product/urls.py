from django.urls import path
from . import views
from dashboard.decorators import user_dashboard_permession
app_name = 'product_dashboard'

urlpatterns = [
    path('create/',user_dashboard_permession(views.CreateProduct.as_view()),
         name='product_create'),
    path('update/<int:pk>/',user_dashboard_permession(views.UpdateProduct.as_view()),
         name='product_update'),
    path('list/', user_dashboard_permession(views.ListProduct.as_view()),
         name='product_list'),
    path('<int:pk>/list/images/', user_dashboard_permession(views.ProductImageList.as_view()),
         name='product_image_list'),
    path('<int:pk>/create/image/',user_dashboard_permession(views.create_image),
         name='create_image'),
]
