# Generated by Django 4.0 on 2021-12-28 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPfinalcoder', '0006_bakery_cake_alter_bakery_date_alter_cakes_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bakery',
            old_name='cake',
            new_name='customer_cake_order',
        ),
        migrations.AlterField(
            model_name='bakery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 17, 29, 21, 356684)),
        ),
        migrations.AlterField(
            model_name='cakes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 17, 29, 21, 356684)),
        ),
        migrations.AlterField(
            model_name='dessert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 17, 29, 21, 356684)),
        ),
    ]
