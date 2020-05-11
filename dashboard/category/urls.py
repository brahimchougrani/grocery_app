from django.urls import path
from . import views
from dashboard.decorators import user_dashboard_permession
app_name = 'category_dashboard'

urlpatterns = [
    path('create/<int:pk>/', user_dashboard_permession(views.CreateSubCategory.as_view()), name="sub_category_create"),
    path('create/', user_dashboard_permession(views.CreateCategory.as_view()), name="category_create"),
    path('update/<int:pk>/', user_dashboard_permession(views.UpdateCategory.as_view()), name="category_update"),
    path('<int:pk>/',user_dashboard_permession( views.categoy_detail), name="category_detail"),
    path('list/', user_dashboard_permession(views.CategoryList.as_view()), name="category_list"),
]
