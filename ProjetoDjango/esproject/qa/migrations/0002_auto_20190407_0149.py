# Generated by Django 2.2 on 2019-04-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='texto',
            field=models.CharField(default='texto-vazio', max_length=1000),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='usuario',
            field=models.CharField(default='usuario vazio', max_length=100),
        ),
    ]
