# Generated by Django 3.0.6 on 2020-05-28 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200525_1935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-id']},
        ),
    ]