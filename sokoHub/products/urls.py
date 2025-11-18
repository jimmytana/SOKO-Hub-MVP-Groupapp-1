from django.urls import path
from .views import addProduct, allProducts, getProduct, vendor_products


urlpatterns = [
    path('add/', addProduct, name='addProduct'),
    path('all/', allProducts, name='allProducts'),
    path('view/someProduct/', getProduct, name='getProduct'),
]