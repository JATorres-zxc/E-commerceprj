# Generated by Django 5.0.1 on 2024-02-08 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]
