# Generated by Django 3.2 on 2022-09-28 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='snippets',
        ),
    ]
