# Generated by Django 3.2.4 on 2021-06-24 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_product_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
