# Generated by Django 4.1 on 2023-05-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=25)),
                ('region', models.CharField(max_length=25)),
                ('town', models.CharField(max_length=25)),
                ('line', models.TextField()),
            ],
        ),
    ]
