from django.urls import path
from . import views
from dashboard.decorators import user_dashboard_permession

app_name = 'brand_dashboard'

urlpatterns = [
    path('create/', user_dashboard_permession(views.CreateBrand.as_view()), name='create_brand'),
    path('update/<int:pk>/',user_dashboard_permession(views.UpdateView.as_view()), name='update_brand'),
    path('list/', user_dashboard_permession(views.ListBrand.as_view()), name='list_brand'),
]