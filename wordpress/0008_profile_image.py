# Generated by Django 3.1.4 on 2021-01-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=None, upload_to='profile', verbose_name='Image : '),
        ),
    ]
