# Generated by Django 4.0.3 on 2022-08-18 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data_created',
            new_name='date_created',
        ),
    ]
