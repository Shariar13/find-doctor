# Generated by Django 3.1.2 on 2021-02-18 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_comment_comment_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_link',
        ),
    ]
