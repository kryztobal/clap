# Generated by Django 2.1.1 on 2018-11-09 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operativos', '0006_auto_20181109_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrega',
            old_name='numero_bolsas',
            new_name='nbolsas',
        ),
    ]
