# Generated by Django 2.2.7 on 2019-12-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_customerpayment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='person_job',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='person_name',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
