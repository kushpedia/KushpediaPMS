# Generated by Django 5.0 on 2024-01-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_rooms_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
