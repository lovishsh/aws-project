# Generated by Django 4.0.5 on 2022-06-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=122, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
