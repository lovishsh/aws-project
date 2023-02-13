# Generated by Django 4.0.5 on 2022-06-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_image_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='shop/images'),
        ),
    ]