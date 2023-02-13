# Generated by Django 4.0.5 on 2022-06-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_rename_order_name_order_name_order_state_order_zip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='order_name',
        ),
        migrations.AlterField(
            model_name='order',
            name='address1',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(max_length=133, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip',
            field=models.CharField(max_length=133, null=True),
        ),
    ]
