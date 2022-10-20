# Generated by Django 3.2.7 on 2022-10-20 02:54

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(default='Paracatu', max_length=180, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='property',
            name='country',
            field=django_countries.fields.CountryField(default='BR', max_length=2, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='property',
            name='postal_code',
            field=models.CharField(default='38600000', max_length=100, verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='property',
            name='street_address',
            field=models.CharField(default='Avenida Olegario Marciel', max_length=150, verbose_name='Street Address'),
        ),
    ]
