# Generated by Django 4.0.3 on 2022-07-04 10:53

import apps.user.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=apps.user.models.avatar_location),
        ),
    ]