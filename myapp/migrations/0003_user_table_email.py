# Generated by Django 3.2.24 on 2024-11-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20241102_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_table',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
