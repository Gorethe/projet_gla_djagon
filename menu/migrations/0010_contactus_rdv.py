# Generated by Django 5.1 on 2024-08-30 13:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_contactus_nbre_de_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='rdv',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
