# Generated by Django 3.2.24 on 2024-11-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_request_table_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_table',
            name='date',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]