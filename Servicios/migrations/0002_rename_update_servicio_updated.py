# Generated by Django 5.0.1 on 2024-01-24 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='update',
            new_name='updated',
        ),
    ]
