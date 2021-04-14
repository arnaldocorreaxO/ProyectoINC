# Generated by Django 2.2.4 on 2019-10-31 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=100, unique=True)),
                ('estados', models.CharField(choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=1)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),

        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=100, unique=True)),
                ('sede', models.CharField(choices=[('CEN', 'CENTRAL'), ('VTA', 'VILLETA'), ('VMI', 'VALLEMI')], default='CEN', max_length=3)),
                ('estados', models.CharField(choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=1)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
                ('dependencia_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_dependencia_padre', to='rh.Dependencia')),
            ],
        ),
    ]
