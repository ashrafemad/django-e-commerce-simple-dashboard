# Generated by Django 2.2.7 on 2019-12-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StartBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.FloatField(verbose_name='Bank balance')),
                ('cash', models.FloatField(verbose_name='Cash balance')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
