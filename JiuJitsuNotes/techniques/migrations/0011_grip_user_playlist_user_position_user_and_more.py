# Generated by Django 4.2.5 on 2023-09-26 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("techniques", "0010_playlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="grip",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="grips",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="playlist",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="playlists",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="position",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="positions",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="submissiontechnique",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="submissions",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="technique",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="techniques",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
