# Generated by Django 4.1.2 on 2022-10-25 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation_blogs',
            name='slug',
        ),
    ]
