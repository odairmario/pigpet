# Generated by Django 2.0.2 on 2018-08-14 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20180814_0137'),
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='membros',
            field=models.ManyToManyField(to='userprofile.UserProfile'),
        ),
    ]
