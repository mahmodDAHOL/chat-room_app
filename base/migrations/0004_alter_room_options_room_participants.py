# Generated by Django 4.1.7 on 2023-03-28 19:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0003_rename_user_room_host"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room", options={"ordering": ["-updated", "-created"]},
        ),
        migrations.AddField(
            model_name="room",
            name="participants",
            field=models.ManyToManyField(
                blank=True, related_name="participants", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
