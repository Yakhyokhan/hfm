# Generated by Django 4.1 on 2023-06-01 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('responsible_group', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsibleperson',
            name='type',
        ),
    ]