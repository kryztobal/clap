# Generated by Django 2.1.1 on 2018-11-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operativos', '0003_auto_20181106_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operativfdo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbolsas', models.IntegerField(default=0)),
            ],
        ),
    ]
