# Generated by Django 3.1.2 on 2021-03-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0036_feed_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_form_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('email', models.CharField(max_length=99)),
                ('message', models.TextField()),
            ],
        ),
    ]