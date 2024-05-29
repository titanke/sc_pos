# Generated by Django 5.0.6 on 2024-05-27 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0015_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posApp.products')),
            ],
        ),
    ]
