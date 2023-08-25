# Generated by Django 4.2.4 on 2023-08-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("techniques", "0002_remove_position_grips_position_their_grips_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="position",
            name="their_grips",
            field=models.ManyToManyField(
                blank=True, related_name="their_grips", to="techniques.grip"
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="your_grips",
            field=models.ManyToManyField(
                blank=True, related_name="your_grips", to="techniques.grip"
            ),
        ),
    ]
