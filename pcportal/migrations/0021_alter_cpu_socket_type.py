# Generated by Django 4.2.19 on 2025-02-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcportal', '0020_casepclisting_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='socket_type',
            field=models.CharField(blank=True, help_text='CPU socket type, (AM4, LGA 1151, etc.)', max_length=30, null=True, verbose_name='CPU socket'),
        ),
    ]
