# Generated by Django 2.2.4 on 2019-08-01 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_admin', models.BooleanField(default=False)),
                ('telefono', models.CharField(blank=True, max_length=30)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='usuarios/fotos')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]