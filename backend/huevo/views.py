from django.http import HttpRequest, HttpResponse
from .models import (
    Billetera, Cliente, Gallina, Granjero, Hotel, Huevo, Stock, Tienda, Venta, VentaHasHuevo
)
from .serializer import (
    BilleteraSerializer, ClienteSerializer, GallinaSerializer, GranjeroSerializer, HotelSerializer, HuevoSerializer, StockSerializer, TiendaSerializer, VentaSerializer, VentaHasHuevoSerializer
)
from rest_framework import generics


