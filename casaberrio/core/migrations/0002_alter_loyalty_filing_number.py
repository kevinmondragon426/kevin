# Generated by Django 4.2.4 on 2023-09-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loyalty',
            name='filing_number',
            field=models.PositiveIntegerField(default=352946, verbose_name='Número de radicado'),
        ),
    ]
