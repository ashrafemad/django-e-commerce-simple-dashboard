# Generated by Django 2.2.7 on 2019-12-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20191216_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Created at'),
        ),
    ]
