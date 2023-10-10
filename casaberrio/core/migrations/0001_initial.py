# Generated by Django 4.2.4 on 2023-09-24 21:44

import core.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('product_code', models.PositiveIntegerField(verbose_name='Codigo de producto')),
                ('product_price', models.PositiveIntegerField(verbose_name='Precio de producto')),
                ('amount', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('product_characteristics', models.TextField(max_length=300, verbose_name='Caracterista de producto')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
                'db_table': 'inventario',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PreferenceContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference_contact', models.CharField(max_length=100, verbose_name='Como prefire ser contactado')),
            ],
            options={
                'verbose_name': 'Como prefire ser contactado',
                'verbose_name_plural': 'Como prefire ser contactado',
                'db_table': 'Como prefire ser contactado',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nombres Completos')),
                ('phone', models.PositiveIntegerField(verbose_name='Numero Celular')),
                ('rental_date_and_time', models.DateField(verbose_name='Fecha y hora de incio')),
                ('return_date_and_time_f', models.DateField(verbose_name='Fecha y hora de finalizacion')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('drink', models.CharField(max_length=200)),
                ('catering', models.CharField(max_length=200)),
                ('equipment', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Alquiler',
                'verbose_name_plural': 'Alquileres',
                'db_table': 'alquiler',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('lastname', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=50, verbose_name='Correo electronico')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='CO', verbose_name='Numero de celular')),
                ('gender', models.CharField(max_length=30)),
                ('event_date', models.DateTimeField(verbose_name='Fecha de evento')),
                ('event_start_time', models.TimeField(verbose_name='Hora inicial del evento')),
                ('theme', models.CharField(max_length=200, verbose_name='Tematica')),
                ('description', models.CharField(max_length=500, verbose_name='Descripcion')),
                ('special_need', models.CharField(max_length=200, verbose_name='Necesidad especial (Personas discapacitadas)')),
                ('guest_document', models.CharField(max_length=200, verbose_name='Documento invitado')),
                ('type_pay', models.CharField(max_length=200)),
                ('eventType', models.CharField(max_length=200)),
                ('campus', models.CharField(max_length=200)),
                ('lounge', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'db_table': 'Reserva',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SelectBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_bank', models.CharField(max_length=20, verbose_name='Seleccion de banco')),
            ],
            options={
                'verbose_name': 'Seleccion de banco',
                'verbose_name_plural': 'Seleccion de bancos',
                'db_table': 'Seleccion de banco',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='StatePqrsd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StatePqrsd', models.CharField(max_length=100, verbose_name='Estado de pqrsd')),
            ],
            options={
                'verbose_name': 'Estado pqrsd',
                'verbose_name_plural': ' Estados pqrsd ',
                'db_table': 'estado pqrsd',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TarjetaDeCD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('card_number', models.PositiveIntegerField(verbose_name='Numero de Tarjeta')),
                ('expiration', models.DateField(verbose_name='Vencimiento')),
            ],
            options={
                'verbose_name': 'Tarjeta de credito y debito',
                'verbose_name_plural': 'Tarjetas de credito y debito',
                'db_table': 'Tarjeta de credito y debito',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypeId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.CharField(max_length=100, verbose_name='Tipo de identificacion')),
            ],
            options={
                'verbose_name': 'Tipo de identificacion',
                'verbose_name_plural': 'Tipo de identificaciones',
                'db_table': 'Tipo de identificacion',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypeOFinput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_input', models.CharField(max_length=100, verbose_name='Tipo de insumo')),
            ],
            options={
                'verbose_name': 'Tipo de insumo',
                'verbose_name_plural': 'Tipo de insumos',
                'db_table': 'Tipo de insumo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypePerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_person', models.CharField(max_length=20, verbose_name='Tipo de persona')),
            ],
            options={
                'verbose_name': 'Tipo de persona',
                'verbose_name_plural': 'Tipo de personas',
                'db_table': 'Tipo de persona',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypePqrsd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_pqrsd', models.CharField(max_length=100, verbose_name='Tipo pqrsd')),
            ],
            options={
                'verbose_name': 'Tipo pqrsd',
                'verbose_name_plural': 'Tipos pqrsd',
                'db_table': 'tipo pqrsd',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.PositiveIntegerField(verbose_name='NIT')),
                ('company_name', models.CharField(max_length=100, verbose_name='Nombre empresa')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.inventory')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedor',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='StateProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(max_length=100, verbose_name='Activo ')),
                ('idle', models.CharField(max_length=100, verbose_name='Inactivo ')),
                ('amount', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('description', models.CharField(max_length=500, verbose_name='Descripcion')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.inventory')),
            ],
            options={
                'verbose_name': 'Estado de producto ',
                'verbose_name_plural': 'Estados de producto ',
                'db_table': 'estadoproducto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PSE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('identification_number', models.PositiveIntegerField(verbose_name='Numero de indentificacion')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Numero de telefono')),
                ('select_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.selectbank')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.typeid')),
                ('type_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.typeperson')),
            ],
            options={
                'verbose_name': 'PSE Cuenta de ahorro y corriente',
                'verbose_name_plural': 'PSE Cuentas de ahorro y corrientes',
                'db_table': 'PSE Cuenta de ahorro y corriente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='loyalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nombres y apellidos')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='CO', verbose_name='Número de teléfono')),
                ('incident_date', models.DateField(verbose_name='Fecha de incidente')),
                ('detailed_description', models.TextField(max_length=300, verbose_name='Descripción detallada')),
                ('product_or_services_name', models.CharField(max_length=50, verbose_name='Nombre de producto/servicio')),
                ('filing_number', models.PositiveIntegerField(default=core.models.generate_random_radicado, verbose_name='Número de radicado')),
                ('preference_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.preferencecontact')),
                ('type_pqrsd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.typepqrsd')),
            ],
            options={
                'verbose_name': 'Fidelizacion',
                'verbose_name_plural': 'Fidelizaciones',
                'db_table': 'fidelizacion',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='inventory',
            name='type_of_input',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.typeofinput'),
        ),
    ]