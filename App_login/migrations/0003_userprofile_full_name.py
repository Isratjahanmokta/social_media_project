# Generated by Django 4.1.3 on 2022-11-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0002_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=265),
        ),
    ]
