# Generated by Django 3.2.24 on 2024-11-02 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_table',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='user_name',
        ),
    ]
