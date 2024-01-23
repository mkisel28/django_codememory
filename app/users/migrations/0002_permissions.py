# Generated by Django 5.0.1 on 2024-01-23 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_add_photos', models.BooleanField(default=False)),
                ('can_add_videos', models.BooleanField(default=False)),
                ('can_add_audio', models.BooleanField(default=False)),
                ('can_add_links', models.BooleanField(default=False)),
                ('can_add_reviews', models.BooleanField(default=False)),
                ('can_add_place_of_birth', models.BooleanField(default=False)),
                ('cann_add_place_of_death', models.BooleanField(default=False)),
                ('can_add_spouse', models.BooleanField(default=False)),
                ('can_add_nationality', models.BooleanField(default=False)),
                ('can_add_occupation', models.BooleanField(default=False)),
                ('can_add_awards', models.BooleanField(default=False)),
                ('can_add_education', models.BooleanField(default=False)),
                ('can_add_family_members', models.BooleanField(default=False)),
                ('can_add_hobbies_interests', models.BooleanField(default=False)),
                ('can_add_life_milestones', models.BooleanField(default=False)),
                ('can_add_personal_anecdotes', models.BooleanField(default=False)),
                ('can_add_significant_places', models.BooleanField(default=False)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.subscription')),
            ],
        ),
    ]