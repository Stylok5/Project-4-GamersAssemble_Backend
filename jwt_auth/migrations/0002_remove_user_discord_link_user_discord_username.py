# Generated by Django 4.2 on 2023-05-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='discord_link',
        ),
        migrations.AddField(
            model_name='user',
            name='discord_username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
