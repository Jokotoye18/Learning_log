# Generated by Django 3.0.5 on 2020-05-03 19:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0010_auto_20200503_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
