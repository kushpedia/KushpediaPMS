# Generated by Django 5.0 on 2024-01-03 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'property', 'verbose_name_plural': 'properties'},
        ),
        migrations.RenameField(
            model_name='property',
            old_name='num_bathrooms',
            new_name='num_rooms',
        ),
    ]
