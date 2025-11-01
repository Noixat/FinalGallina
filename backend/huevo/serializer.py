from rest_framework import serializers
from .models import (
    Billetera, Cliente, Gallina, Granjero, Hotel, Huevo, Stock, Tienda, Venta, VentaHasHuevo
)
#que modelos quiero que interactuen con angular, acá pusimos todo
class BilleteraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billetera
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class GallinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallina
        fields = '__all__'

class GranjeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Granjero
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class HuevoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huevo
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class VentaHasHuevoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaHasHuevo
        fields = '__all__'