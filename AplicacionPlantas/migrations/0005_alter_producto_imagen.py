# Generated by Django 5.0.6 on 2024-06-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplicacionPlantas', '0004_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
