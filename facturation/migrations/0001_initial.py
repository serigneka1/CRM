# Generated by Django 4.2.1 on 2023-06-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
