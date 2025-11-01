from django.db import models

#Acá primero creamos la base de datos en phpmyadmin, luego las traspasmos al proyecto de django y se auto_generaron los models como resultado. Es mas facil crear los models primero.
class Billetera(models.Model):
    venta_total_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='Venta_total_venta')  # Field name made lowercase.
    ganancia = models.CharField(max_length=45)
    alimentacion_gall = models.CharField(db_column='Alimentacion_gall', primary_key=True, max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'billetera'


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    estado_cliente = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'cliente'


class Gallina(models.Model):
    idgallina = models.AutoField(db_column='idGallina', primary_key=True)  # Field name made lowercase.
    nom_gallina = models.CharField(max_length=20)

    class Meta:
        db_table = 'gallina'


class Granjero(models.Model):
    gallina_idgallina = models.ForeignKey(Gallina, models.DO_NOTHING, db_column='Gallina_idGallina')  # Field name made lowercase.
    nom_granjero = models.CharField(primary_key=True, max_length=20)

    class Meta:
        db_table = 'granjero'


class Hotel(models.Model):
    billetera_alimentacion_gall = models.ForeignKey(Billetera, models.DO_NOTHING, db_column='Billetera_Alimentacion_gall')  # Field name made lowercase.

    class Meta:
        db_table = 'hotel'


class Huevo(models.Model):
    idhuevo = models.IntegerField(db_column='idHuevo', primary_key=True)  # Field name made lowercase.
    tamano = models.CharField(db_column='Tamano', max_length=10)  # Field name made lowercase.
    gallina_idgallina = models.ForeignKey(Gallina, models.DO_NOTHING, db_column='Gallina_idGallina')  # Field name made lowercase.

    class Meta:
        db_table = 'huevo'


class Stock(models.Model):
    stock_total = models.IntegerField(db_column='Stock_total', primary_key=True)  # Field name made lowercase.
    huevo_idhuevo = models.ForeignKey(Huevo, models.DO_NOTHING, db_column='Huevo_idHuevo')  # Field name made lowercase.

    class Meta:
        db_table = 'stock'


class Tienda(models.Model):
    fecha_venta = models.DateTimeField(db_column='Fecha_venta', primary_key=True)  # Field name made lowercase.
    stock_stock_total = models.ForeignKey(Stock, models.DO_NOTHING, db_column='Stock_Stock_total')  # Field name made lowercase.

    class Meta:
        db_table = 'tienda'


class Venta(models.Model):
    tienda_fecha_venta = models.ForeignKey(Tienda, models.DO_NOTHING, db_column='Tienda_Fecha_venta')  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_idCliente')  # Field name made lowercase.
    total_venta = models.CharField(primary_key=True, max_length=9)
    granjero_nom_granjero = models.ForeignKey(Granjero, models.DO_NOTHING, db_column='Granjero_nom_granjero')  # Field name made lowercase.

    class Meta:
        db_table = 'venta'


class VentaHasHuevo(models.Model):
    venta_total_venta = models.ForeignKey(Venta, models.DO_NOTHING, db_column='Venta_total_venta')  # Field name made lowercase.
    huevo_idhuevo = models.ForeignKey(Huevo, models.DO_NOTHING, db_column='Huevo_idHuevo')  # Field name made lowercase.
    precio = models.CharField(max_length=20, blank=True, null=True)
    id_vhh = models.CharField(primary_key=True, max_length=45)

    class Meta:
        db_table = 'venta_has_huevo'