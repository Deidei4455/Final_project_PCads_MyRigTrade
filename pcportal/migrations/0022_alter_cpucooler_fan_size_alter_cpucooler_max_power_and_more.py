# Generated by Django 4.2.19 on 2025-02-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcportal', '0021_alter_cpu_socket_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpucooler',
            name='fan_size',
            field=models.IntegerField(blank=True, help_text='CPU cooler fan size, mm', null=True, verbose_name='Fan size'),
        ),
        migrations.AlterField(
            model_name='cpucooler',
            name='max_power',
            field=models.IntegerField(blank=True, help_text='Max CPU cooler power, W', null=True, verbose_name='Max power'),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='max_ram',
            field=models.IntegerField(blank=True, help_text='Max RAM capacity that motherboard can have', null=True, verbose_name='Max RAM'),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='socket_type',
            field=models.CharField(blank=True, help_text='CPU socket type, (AM4, LGA 1151, etc.)', max_length=30, null=True, verbose_name='Socket type'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='ram_speed',
            field=models.IntegerField(blank=True, help_text='RAM speed, MHz', null=True, verbose_name='RAM speed'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='read_speed',
            field=models.IntegerField(blank=True, help_text='Read speed MB/s', null=True, verbose_name='Read speed'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='write_speed',
            field=models.IntegerField(blank=True, help_text='Write speed MB/s', null=True, verbose_name='Write speed'),
        ),
    ]
