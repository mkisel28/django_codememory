# Generated by Django 5.0.1 on 2024-01-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="memorypage",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="photo/avatars/"),
        ),
    ]