# Generated by Django 2.0.2 on 2018-08-13 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupospet', '0001_initial'),
        ('userprofile', '0004_auto_20180813_0041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='tipoUsuario',
            new_name='tipo_usuario',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='grupoPet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='grupospet.GrupoPet'),
            preserve_default=False,
        ),
    ]
