# Generated by Django 4.0.5 on 2022-06-21 11:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_alter_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(default=datetime.datetime(2022, 6, 21, 11, 33, 9, 692540, tzinfo=utc), primary_key=True, serialize=False),
        ),
    ]
