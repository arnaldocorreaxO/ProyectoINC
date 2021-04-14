# Generated by Django 2.2.4 on 2019-09-26 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0002_documento_publicacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='publicacion',
            options={'verbose_name': 'Publicacion', 'verbose_name_plural': 'Publicaciones'},
        ),
        migrations.RemoveField(
            model_name='documento',
            name='fecIns',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='fecUpd',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='usuIns',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='usuUpd',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='fecIns',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='fecUpd',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='usuIns',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='usuUpd',
        ),
    ]
