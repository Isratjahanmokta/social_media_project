# Generated by Django 4.1.3 on 2022-11-25 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0003_userprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
