from django.urls import path
from .views import ProductListCreate
from .views import product_list

urlpatterns = [
    # path('products/', ProductListCreate.as_view()),
    path('products/', product_list),
]
