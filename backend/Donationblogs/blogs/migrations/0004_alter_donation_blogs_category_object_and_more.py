# Generated by Django 4.1.2 on 2022-10-28 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_donation_blogs_category_object_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation_blogs',
            name='category_object',
            field=models.CharField(choices=[('CLOTHES', 'Clothes'), ('SHOSE', 'Shose'), ('FOODANDDRUG', 'Foodanddrug'), ('DONATION', 'Donation'), ('APPLIANCE', 'Appliance')], default='APPLIANCE', max_length=50),
        ),
        migrations.AlterField(
            model_name='donation_blogs',
            name='category_user',
            field=models.CharField(choices=[('KID', 'Kid'), ('TEENAGER', 'Teenager'), ('ADULT', 'Adult'), ('GRAYBEARD', 'Graybeard'), ('CRIPPLE', 'Cripple')], default='KID', max_length=50),
        ),
    ]
