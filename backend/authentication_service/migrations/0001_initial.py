# Generated by Django 5.0.2 on 2024-02-21 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=10)),
                ('address', models.TextField(default='')),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('zip_code', models.CharField(default='', max_length=10)),
                ('image_url', models.CharField(default='', max_length=100)),
                ('password_hash', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client_id', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField(default='')),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('zip_code', models.CharField(default='', max_length=10)),
                ('image_url', models.CharField(default='', max_length=200)),
                ('specific_focus_areas', models.CharField(default='', max_length=50)),
                ('lawyer_resume', models.CharField(default='', max_length=100)),
                ('lawyer_bio', models.TextField(default='')),
                ('password_hash', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lawyer_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Lawyer',
                'verbose_name_plural': 'Lawyers',
                'db_table': 'Lawyer',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('practice_area_id', models.AutoField(primary_key=True, serialize=False)),
                ('practice_area_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'db_table': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review', models.TextField()),
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication_service.client')),
                ('lawyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication_service.lawyer')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'db_table': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Lawyer_practice_areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lawyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication_service.lawyer')),
                ('practice_area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication_service.roles')),
            ],
            options={
                'verbose_name': 'Lawyer Practice Area',
                'verbose_name_plural': 'Lawyer Practice Areas',
                'db_table': 'Lawyer_practice_areas',
            },
        ),
    ]
