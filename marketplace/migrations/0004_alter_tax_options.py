# Generated by Django 4.1.1 on 2022-11-07 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_tax'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tax',
            options={'verbose_name_plural': 'Tax'},
        ),
    ]