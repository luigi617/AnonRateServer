# Generated by Django 4.0.3 on 2022-08-11 07:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_avatar_thumbnail_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ManyToManyField(related_name='labels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
