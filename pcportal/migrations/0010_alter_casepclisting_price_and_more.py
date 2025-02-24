# Generated by Django 4.2.19 on 2025-02-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcportal', '0009_alter_casepclisting_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casepclisting',
            name='price',
            field=models.FloatField(verbose_name='Price per piece'),
        ),
        migrations.AlterField(
            model_name='cpucoolerlisting',
            name='price',
            field=models.FloatField(verbose_name='Price per piece'),
        ),
        migrations.AlterField(
            model_name='cpulisting',
            name='price',
            field=models.FloatField(verbose_name='Price per piece'),
        ),
        migrations.AlterField(
            model_name='gpulisting',
            name='price',
            field=models.FloatField(verbose_name='Price per piece'),
        ),
        migrations.AlterField(
            model_name='motherboardlisting',
            name='price',
            field=models.FloatField(verbose_name='Price per piece'),
        ),
        migrations.AlterField(
            model_name='psulisting',
            name='price',
            field=models.FloatField(verbose_name='Price per piece'),
        ),
        migrations.AlterField(
            model_name='ramlisting',
            name='price',
            field=models.FloatField(verbose_name='Price per piece'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone_num',
            field=models.IntegerField(max_length=10, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='storagelisting',
            name='price',
            field=models.FloatField(verbose_name='Price per piece'),
        ),
    ]
