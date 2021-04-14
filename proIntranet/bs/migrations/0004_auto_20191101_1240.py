# Generated by Django 2.2.4 on 2019-11-01 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bs', '0003_auto_20191101_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bs.Departamento'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bs.Pais'),
        ),
    ]
