# Generated by Django 5.1.4 on 2025-01-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0005_customuser_groups_customuser_user_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('vehicle_name', models.CharField(max_length=200)),
                ('model_name', models.CharField(max_length=200)),
                ('manufacturer_name', models.CharField(max_length=200)),
                ('product_condition', models.CharField(max_length=50)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('product_video', models.FileField(blank=True, null=True, upload_to='product_videos/')),
                ('predicted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
