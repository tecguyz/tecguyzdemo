# Generated by Django 3.1.4 on 2021-03-25 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecguyz', '0006_remove_trending_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='trending',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
