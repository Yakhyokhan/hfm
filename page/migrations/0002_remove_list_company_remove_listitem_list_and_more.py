# Generated by Django 4.1 on 2023-06-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='company',
        ),
        migrations.RemoveField(
            model_name='listitem',
            name='list',
        ),
        migrations.AlterField(
            model_name='page',
            name='inputs',
            field=models.JSONField(null=True),
        ),
    ]
