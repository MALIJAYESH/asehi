# Generated by Django 3.0.6 on 2020-06-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
