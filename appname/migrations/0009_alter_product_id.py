# Generated by Django 5.1.4 on 2025-01-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0008_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
