# Generated by Django 2.2.4 on 2019-10-31 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.DeleteModel(
            name='Dependencia',
        ),
    ]