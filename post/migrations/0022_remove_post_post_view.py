# Generated by Django 3.1.2 on 2021-02-16 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_post_post_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_view',
        ),
    ]
