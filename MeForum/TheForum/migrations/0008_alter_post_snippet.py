# Generated by Django 4.2.4 on 2023-11-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheForum', '0007_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
