# Generated by Django 4.2.5 on 2023-12-10 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_userprofile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='followers_count',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='following_count',
        ),
    ]
