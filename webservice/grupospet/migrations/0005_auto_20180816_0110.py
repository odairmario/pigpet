# Generated by Django 2.0.2 on 2018-08-16 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupospet', '0004_auto_20180814_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupopet',
            name='projetos',
            field=models.ManyToManyField(blank=True, null=True, related_name='grupos_pet', to='projetos.Projeto'),
        ),
    ]