from django.urls import path
from .views import addProduct, allProducts
urlpatterns = [
    path('add', addProduct, name='addProduct'),
    path('all', allProducts, name='allProducts')
]