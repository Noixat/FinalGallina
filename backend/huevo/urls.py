from django.urls import path
from django import urls
from .views import (
    BilleteraListCreate, BilleteraRetrieveUpdateDestroy,
    ClienteListCreate, ClienteRetrieveUpdateDestroy,
    GallinaListCreate, GallinaRetrieveUpdateDestroy,
    GranjeroListCreate, GranjeroRetrieveUpdateDestroy,
    HotelListCreate, HotelRetrieveUpdateDestroy,
    HuevoListCreate, HuevoRetrieveUpdateDestroy,
    StockListCreate, StockRetrieveUpdateDestroy,
    TiendaListCreate, TiendaRetrieveUpdateDestroy,
    VentaListCreate, VentaRetrieveUpdateDestroy,
    VentaHasHuevoListCreate, VentaHasHuevoRetrieveUpdateDestroy
)

urlpatterns = [
    path('billetera/', BilleteraListCreate.as_view(), name='billetera-list-create'),
    path('billetera/<int:pk>/', BilleteraRetrieveUpdateDestroy.as_view(), name='billetera-re-up-de'),
    
    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-re-up-de'),
    
    path('gallinas/', GallinaListCreate.as_view(), name='gallina-list-create'),
    path('gallinas/<int:pk>/', GallinaRetrieveUpdateDestroy.as_view(), name='gallina-re-up-de'),
    
    path('granjero/', GranjeroListCreate.as_view(), name='granjero-list-create'),
    path('granjero/<int:pk>/', GranjeroRetrieveUpdateDestroy.as_view(), name='granjero-re-up-de'),
    
    path('hotele/', HotelListCreate.as_view(), name='hotel-list-create'),
    path('hotele/<int:pk>/', HotelRetrieveUpdateDestroy.as_view(), name='hotel-re-up-de'),
    
    path('huevos/', HuevoListCreate.as_view(), name='huevo-list-create'),
    path('huevos/<int:pk>/', HuevoRetrieveUpdateDestroy.as_view(), name='huevo-re-up-de'),
    
    path('stock/', StockListCreate.as_view(), name='stock-list-create'),
    path('stock/<int:pk>/', StockRetrieveUpdateDestroy.as_view(), name='stock-re-up-de'),
    
    path('tienda/', TiendaListCreate.as_view(), name='tienda-list-create'),
    path('tienda/<int:pk>/', TiendaRetrieveUpdateDestroy.as_view(), name='tienda-re-up-de'),
    
    path('ventas/', VentaListCreate.as_view(), name='venta-list-create'),
    path('ventas/<int:pk>/', VentaRetrieveUpdateDestroy.as_view(), name='venta-re-up-de'),
    
    path('venta-huevo/', VentaHasHuevoListCreate.as_view(), name='venta-huevo-list-create'),
    path('venta-huevo/<int:pk>/', VentaHasHuevoRetrieveUpdateDestroy.as_view(), name='venta-huevo-re-up-de'),
]