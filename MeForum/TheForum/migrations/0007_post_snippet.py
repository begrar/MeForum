# Generated by Django 4.2.7 on 2023-11-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheForum', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above To Read Forum Post...', max_length=255),
        ),
    ]
