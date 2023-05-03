# Generated by Django 4.2 on 2023-05-03 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ratings', '0006_remove_rating_disliked_by_remove_rating_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='disliked_by',
            field=models.ManyToManyField(blank=True, related_name='disliked_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ratings_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
