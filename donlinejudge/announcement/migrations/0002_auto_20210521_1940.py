# Generated by Django 3.1 on 2021-05-21 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-creation_time']},
        ),
        migrations.AlterModelTable(
            name='announcement',
            table='announcement',
        ),
    ]
