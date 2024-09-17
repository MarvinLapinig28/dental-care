# Generated by Django 5.1 on 2024-09-14 05:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customuser_address_customuser_contact_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('valid_id', models.ImageField(null=True, upload_to='media/uploads')),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
