# Generated by Django 2.2.7 on 2019-11-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20191130_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpayment',
            name='cuts',
            field=models.FloatField(default=0, verbose_name='إستقطاعات'),
        ),
        migrations.AlterField(
            model_name='customerpayment',
            name='fines',
            field=models.FloatField(default=0, verbose_name='غرامات'),
        ),
        migrations.AlterField(
            model_name='customerpayment',
            name='perks',
            field=models.FloatField(default=0, verbose_name='إكراميات'),
        ),
    ]
