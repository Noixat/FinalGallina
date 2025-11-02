from django.http import HttpRequest, HttpResponse
from rest_framework import generics
from .models import (
    Billetera, Cliente, Gallina, Granjero, Hotel, Huevo, Stock, Tienda, Venta, VentaHasHuevo
)
from .serializer import (
    BilleteraSerializer, ClienteSerializer, GallinaSerializer, GranjeroSerializer, HotelSerializer, HuevoSerializer, StockSerializer, TiendaSerializer, VentaSerializer, VentaHasHuevoSerializer
)
#Read y Create
class BilleteraListCreate(generics.ListCreateAPIView):
    queryset = Billetera.objects.all()
    serializer_class = BilleteraSerializer
#Read Update Delete
class BilleteraRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billetera.objects.all()
    serializer_class = BilleteraSerializer

class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class GallinaListCreate(generics.ListCreateAPIView):
    queryset = Gallina.objects.all()
    serializer_class = GallinaSerializer

class GallinaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallina.objects.all()
    serializer_class = GallinaSerializer

class GranjeroListCreate(generics.ListCreateAPIView):
    queryset = Granjero.objects.all()
    serializer_class = GranjeroSerializer

class GranjeroRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Granjero.objects.all()
    serializer_class = GranjeroSerializer

class HotelListCreate(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HuevoListCreate(generics.ListCreateAPIView):
    queryset = Huevo.objects.all()
    serializer_class = HuevoSerializer

class HuevoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Huevo.objects.all()
    serializer_class = HuevoSerializer

class StockListCreate(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class TiendaListCreate(generics.ListCreateAPIView):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

class TiendaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

class VentaListCreate(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaHasHuevoListCreate(generics.ListCreateAPIView):
    queryset = VentaHasHuevo.objects.all()
    serializer_class = VentaHasHuevoSerializer

class VentaHasHuevoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VentaHasHuevo.objects.all()
    serializer_class = VentaHasHuevoSerializer