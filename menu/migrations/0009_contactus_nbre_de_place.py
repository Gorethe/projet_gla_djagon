# Generated by Django 5.1 on 2024-08-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_chef_name_alter_contactus_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='nbre_de_place',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]