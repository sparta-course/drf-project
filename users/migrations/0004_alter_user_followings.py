# Generated by Django 4.1.2 on 2022-11-05 07:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_followings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
