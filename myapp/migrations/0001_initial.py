# Generated by Django 3.2.24 on 2024-11-02 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='camp_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('capacity', models.BigIntegerField()),
                ('details', models.CharField(max_length=100)),
                ('lattitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='coordinator_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=30)),
                ('phone_number', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
                ('CAMP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.camp_table')),
            ],
        ),
        migrations.CreateModel(
            name='emergency_response_team_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('experience', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='goods_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('details', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('COORDINATOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.coordinator_table')),
            ],
        ),
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('details', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='services_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='volunteer_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
                ('dob', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='request_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('EMERGENCY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.emergency_response_team_table')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user_table')),
            ],
        ),
        migrations.CreateModel(
            name='needs_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('COORDINATOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.coordinator_table')),
                ('GOODS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.goods_table')),
            ],
        ),
        migrations.CreateModel(
            name='medical_support_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('COORDINATOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.coordinator_table')),
            ],
        ),
        migrations.CreateModel(
            name='item_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('picture', models.FileField(upload_to='')),
                ('status', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='guideline_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guidelines', models.FileField(upload_to='')),
                ('details', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('COORDINATOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.coordinator_table')),
            ],
        ),
        migrations.AddField(
            model_name='emergency_response_team_table',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login_table'),
        ),
        migrations.AddField(
            model_name='coordinator_table',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login_table'),
        ),
        migrations.CreateModel(
            name='complaint_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaints', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('CAMP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.camp_table')),
                ('COORDINATOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.coordinator_table')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user_table')),
            ],
        ),
    ]
