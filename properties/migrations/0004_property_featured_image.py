# Generated by Django 5.0 on 2024-01-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_property_num_of_floors'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]