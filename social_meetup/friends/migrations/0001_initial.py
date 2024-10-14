# Generated by Django 5.1 on 2024-10-12 00:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('request_from', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='request_from', to=settings.AUTH_USER_MODEL)),
                ('request_to', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='request_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
