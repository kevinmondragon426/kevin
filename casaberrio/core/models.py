from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
import random
from django.contrib.auth.models import User







class Reserva(models.Model):
    TEMATICA_CHOICES = (
    ('Campestre', 'Campestre'),
    ('Neon', 'Neon'),
    ('Alfombra_Roja', 'Alfombra Roja'),
    ('Personaje_Disney', 'Personaje Disney'),
    ('Flores', 'Flores'),
    ('Noche_estrellas', 'Noche de Estrellas'),
    ('Tropical', 'Tropical'),
    ('Mariposas', 'Mariposas'),
)


    name = models.CharField(max_length=50,verbose_name='Nombres', )
    lastname = models.CharField(max_length=50, verbose_name='Apellidos')
    email = models.EmailField(max_length=50, verbose_name='Correo electronico')
    phone = PhoneNumberField(verbose_name='Numero de celular',region='CO')
    gender = models.CharField(max_length=30, verbose_name='Genero')
    event_date = models.DateTimeField( verbose_name='Fecha de evento')
    event_start_time = models.TimeField(verbose_name='Hora inicial del evento')
    theme = models.CharField(max_length=200, verbose_name='Tematica',choices=TEMATICA_CHOICES,default='Mariposas')
    description = models.CharField(max_length=500,  verbose_name='Descripcion', help_text= 'Descipcion del evento Mas detallado ')
    special_need = models.CharField(max_length=200, verbose_name='Necesidad especial (Personas discapacitadas)')
    eventType = models.CharField (max_length=200, verbose_name='Tipo de evento')
    campus = models.CharField (max_length=200, verbose_name='Sede' )
    lounge = models.CharField(max_length=200,verbose_name='Salón' )
    
    def __str__(self):
        return str(self.event_date)
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        db_table = 'Reserva'
        ordering = ['id']  
            
class TypeId(models.Model):
    type_id = models.CharField(max_length=100, verbose_name='Tipo de identificacion')
    
    def __str__(self):
        return self.type_id

    class Meta:
        verbose_name = 'Tipo de identificacion'
        verbose_name_plural = 'Tipo de identificaciones'
        db_table = 'Tipo de identificacion'
        ordering = ['id']
            
class SelectBank(models.Model):
    select_bank = models.CharField(max_length=20, verbose_name='Seleccion de banco')
    
    def __str__(self):
        return self.select_bank

    class Meta:
        verbose_name = 'Seleccion de banco'
        verbose_name_plural = 'Seleccion de bancos'
        db_table = 'Seleccion de banco'
        ordering = ['id']
        
class TypePerson(models.Model):
    type_person = models.CharField(max_length=20, verbose_name='Tipo de persona')
    
    def __str__(self):
        return self.type_person

    class Meta:
        verbose_name = 'Tipo de persona'
        verbose_name_plural = 'Tipo de personas'
        db_table = 'Tipo de persona'
        ordering = ['id']
    
class PSE(models.Model):
    type_person = models.ForeignKey(TypePerson, on_delete=models.CASCADE,verbose_name='Tipo de persona')
    select_bank = models.ForeignKey(SelectBank, on_delete=models.CASCADE, verbose_name='Seleccione su Banco')
    full_name = models.CharField(max_length=100, verbose_name='Nombre Completo')
    type_id = models.ForeignKey(TypeId,on_delete=models.CASCADE, verbose_name='Tipo de Identificación')
    identification_number= models.PositiveIntegerField(verbose_name='Numero de indentificacion')
    email = models.EmailField(verbose_name='Correo electronico')
    phone_number = PhoneNumberField(verbose_name='Numero de telefono')
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'PSE Cuenta de ahorro y corriente'
        verbose_name_plural = 'PSE Cuentas de ahorro y corrientes'
        db_table = 'PSE Cuenta de ahorro y corriente'
        ordering = ['id']
        
class TarjetaDeCD(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Nombre Completo')
    card_number= models.PositiveIntegerField(verbose_name='Numero de Tarjeta')
    expiration = models.CharField(verbose_name='Vencimiento', max_length=5)
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Tarjeta de credito y debito'
        verbose_name_plural = 'Tarjetas de credito y debito'
        db_table = 'Tarjeta de credito y debito'
        ordering = ['id']
 
class Carrito(models.Model):
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Nombre de usuario')
    elementos_alquilar =  models.TextField(max_length=1000 , verbose_name='Elementos seleccionados')
    precio_total = models.IntegerField(verbose_name='Precio Total')
    
    def __str__(self):
        return str(self.nombre_usuario)

    class Meta:
        verbose_name = 'Carrito Alquiler'
        verbose_name_plural = 'Carrito de Alquileres'
        db_table = 'Carrito_alquiler'
        ordering = ['id']


class TypeOFinput(models.Model):
    type_of_input = models.CharField(max_length=100,verbose_name= 'Tipo de insumo')
    
    def __str__(self):
        return self.type_of_input

    class Meta:
        verbose_name='Tipo de insumo'
        verbose_name_plural='Tipo de insumos'
        db_table='Tipo de insumo'
        ordering=['id']

class Inventory(models.Model):
    type_of_input = models.ForeignKey(TypeOFinput, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100,verbose_name ='Nombre del producto')
    product_code = models.PositiveIntegerField(verbose_name='Codigo de producto')
    product_price = models.PositiveIntegerField (verbose_name='Precio de producto')
    amount = models.PositiveIntegerField(verbose_name='Cantidad')
    product_characteristics = models.TextField(max_length=300, verbose_name='Caracterista de producto')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name='Inventario'
        verbose_name_plural='Inventarios'
        db_table='inventario'
        ordering=['id']

class Supplier (models.Model):
    nit = models.PositiveIntegerField(verbose_name = 'NIT')
    company_name = models.CharField(max_length =100, verbose_name = 'Nombre empresa')
    inventory = models.ForeignKey (Inventory, on_delete=models.CASCADE)

    def __str__ (self):
        return self.company_name

    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'
        db_table='proveedor'
        ordering=['id']



class StateProduct(models.Model):
    ESTADOP_CHOICES = (
        ('Activo ', 'Activo '),
        ('Inactivo ', 'Inactivo '),
    )
    estadoP = models.CharField(max_length=20, choices=ESTADOP_CHOICES, default='Activo ')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.estadoP

    class Meta:
        verbose_name = 'Estado Producto'
        verbose_name_plural = 'Estados productos'
        db_table = 'estado_producto'
        ordering = ['id']

        
class TypePqrsd(models.Model):
    type_pqrsd = models.CharField(max_length=100,verbose_name= 'Tipo pqrsd')
    
    def __str__(self):
        return self.type_pqrsd

    class Meta:
        verbose_name='Tipo pqrsd'
        verbose_name_plural='Tipos pqrsd'
        db_table='tipo pqrsd'
        ordering=['id']
        
               
class PreferenceContact(models.Model):
    preference_contact = models.CharField(max_length=100,verbose_name= 'Como prefire ser contactado')
    
    def __str__(self):
        return self.preference_contact

    class Meta:
        verbose_name='Como prefire ser contactado'
        verbose_name_plural='Como prefire ser contactado'
        db_table='Como prefire ser contactado'
        ordering=['id']


def generate_random_radicado():
    return random.randint(100000, 999999)

class loyalty(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Nombres y apellidos')
    email = models.EmailField(verbose_name='Correo electrónico')
    phone = PhoneNumberField(verbose_name='Número de teléfono', region='CO')
    type_pqrsd = models.ForeignKey(TypePqrsd, on_delete=models.CASCADE,verbose_name='Tipo de PQRSD')
    incident_date = models.DateField(verbose_name='Fecha de incidente')
    detailed_description = models.TextField(max_length=300, verbose_name='Descripción detallada')
    product_or_services_name = models.CharField(max_length=50, verbose_name='Nombre de producto/servicio')
    filing_number = models.PositiveIntegerField(verbose_name='Guarde el Número de radicado para consultar el estado de su PQRSD', default=generate_random_radicado,)  
    preference_contact = models.ForeignKey(PreferenceContact, on_delete=models.CASCADE, verbose_name='Como prefiere ser contactad@', help_text='&nbsp')

    def __str__(self):
        return str(self.filing_number)

    def save(self, *args, **kwargs):
        if not self.filing_number:
          
            self.filing_number = random.randint(100000, 999999)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Fidelizacion'
        verbose_name_plural = 'Fidelizaciones'
        db_table = 'fidelizacion'
        ordering = ['id']

  

class StatePqrsd(models.Model):
    ESTADO_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Resuelto', 'Resuelto'),
        ('Cerrado', 'Cerrado'),
    )
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    loyalty = models.ForeignKey(loyalty, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = 'Estado pqrsd'
        verbose_name_plural = 'Estados pqrsd'
        db_table = 'estado_pqrsd'
        ordering = ['id']



    
