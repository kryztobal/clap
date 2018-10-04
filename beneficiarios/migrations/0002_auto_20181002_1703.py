# Generated by Django 2.1.1 on 2018-10-02 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='beneficiarios',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beneficiarios.Cargo'),
        ),
    ]
