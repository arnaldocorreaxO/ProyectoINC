# Generated by Django 2.2.4 on 2019-10-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_auto_20191022_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='genero',
            field=models.CharField(blank=True, choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=1, null=True),
        ),
    ]