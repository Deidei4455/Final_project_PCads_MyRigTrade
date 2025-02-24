# Generated by Django 4.2.19 on 2025-02-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcportal', '0026_sellerreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casepclisting',
            name='expiration_date',
            field=models.DateField(default='2025-03-20', verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='cpucoolerlisting',
            name='expiration_date',
            field=models.DateField(default='2025-03-20', verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='cpulisting',
            name='expiration_date',
            field=models.DateField(default='2025-03-20', verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='gpulisting',
            name='expiration_date',
            field=models.DateField(default='2025-03-20', verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='motherboardlisting',
            name='expiration_date',
            field=models.DateField(default='2025-03-20', verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='psulisting',
            name='expiration_date',
            field=models.DateField(default='2025-03-20', verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='ramlisting',
            name='expiration_date',
            field=models.DateField(default='2025-03-20', verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='storagelisting',
            name='expiration_date',
            field=models.DateField(default='2025-03-20', verbose_name='Expiration date'),
        ),
    ]
