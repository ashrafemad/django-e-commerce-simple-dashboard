# Generated by Django 2.2.7 on 2020-01-03 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0015_customerpayment_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerWithBalance',
            fields=[
            ],
            options={
                'verbose_name': 'مدين',
                'verbose_name_plural': 'مدينين',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('customers.customer',),
        ),
    ]