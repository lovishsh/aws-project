# Generated by Django 4.0.5 on 2022-06-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_updateorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateorder',
            name='order_id',
            field=models.CharField(max_length=122, null=True),
        ),
    ]