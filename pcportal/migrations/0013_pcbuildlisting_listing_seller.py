# Generated by Django 4.2.19 on 2025-02-20 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pcportal', '0012_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcbuildlisting',
            name='listing_seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
