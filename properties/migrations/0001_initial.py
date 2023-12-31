# Generated by Django 5.0 on 2024-01-03 06:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('num_bathrooms', models.PositiveIntegerField(blank=True, null=True)),
                ('year_built', models.PositiveIntegerField(blank=True, null=True)),
                ('latitudes', models.FloatField(blank=True, null=True)),
                ('longitudes', models.FloatField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
