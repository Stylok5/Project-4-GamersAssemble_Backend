# Generated by Django 4.2 on 2023-05-03 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
