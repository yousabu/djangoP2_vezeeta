# Generated by Django 3.1.4 on 2021-01-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210101_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=None, upload_to='profile', verbose_name='Image : '),
        ),
    ]
