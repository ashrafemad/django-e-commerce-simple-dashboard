# Generated by Django 2.2.7 on 2019-12-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20191130_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerpayment',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
