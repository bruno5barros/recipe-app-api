# Generated by Django 2.1.15 on 2021-04-15 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ingridient'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingridient',
            new_name='Ingredient',
        ),
    ]
