# Generated by Django 4.2.1 on 2023-06-06 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',)},
        ),
    ]
