# Generated by Django 3.2.4 on 2021-07-24 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='full_name',
        ),
    ]
