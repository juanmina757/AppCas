# Generated by Django 4.1 on 2023-03-24 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas', '0002_profile_image_alter_profile_bio_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Hola, twitter', max_length=100),
        ),
    ]
