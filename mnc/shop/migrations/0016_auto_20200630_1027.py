# Generated by Django 3.0.6 on 2020-06-30 04:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20200630_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AddField(
            model_name='contact',
            name='msg_id',
            field=models.AutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
