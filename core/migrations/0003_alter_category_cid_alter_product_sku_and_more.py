# Generated by Django 5.0.1 on 2024-02-02 14:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_product_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
