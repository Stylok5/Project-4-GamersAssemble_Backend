# Generated by Django 4.2 on 2023-05-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
