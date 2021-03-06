# Generated by Django 2.2.7 on 2019-11-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_customerpayment_customerpaymentcut_customerpaymentcutvalue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerpaymentcutvalue',
            name='cut',
        ),
        migrations.AddField(
            model_name='customerpayment',
            name='fines',
            field=models.FloatField(blank=True, null=True, verbose_name='غرامات'),
        ),
        migrations.AddField(
            model_name='customerpayment',
            name='perks',
            field=models.FloatField(blank=True, null=True, verbose_name='إكراميات'),
        ),
        migrations.RemoveField(
            model_name='customerpayment',
            name='cuts',
        ),
        migrations.AddField(
            model_name='customerpayment',
            name='cuts',
            field=models.FloatField(blank=True, null=True, verbose_name='إستقطاعات'),
        ),
        migrations.DeleteModel(
            name='CustomerPaymentCut',
        ),
        migrations.DeleteModel(
            name='CustomerPaymentCutValue',
        ),
    ]
