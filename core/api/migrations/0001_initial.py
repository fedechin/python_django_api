# Generated by Django 5.0.1 on 2024-01-17 17:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('categories', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('icon_url', models.URLField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField()),
                ('value', models.TextField()),
            ],
        ),
    ]
