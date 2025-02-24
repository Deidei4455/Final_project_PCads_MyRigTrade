# Generated by Django 4.2.19 on 2025-02-22 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pcportal', '0014_casepclisting_listing_seller_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
