# Generated by Django 3.1.2 on 2021-02-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20210213_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]