# Generated by Django 4.2 on 2025-07-05 11:59

import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('mobile_number', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('display_picture', models.ImageField(blank=True, default='', null=True, upload_to='Display Picture')),
                ('orders', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None)),
                ('following', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250, null=True), default=list, size=None)),
                ('wish_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250, null=True), default=list, size=None)),
                ('billing_address', models.CharField(default='', max_length=250)),
                ('city', models.CharField(default='', max_length=250)),
                ('state', models.CharField(default='', max_length=250)),
                ('zip', models.CharField(default='', max_length=250)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2025, 7, 5, 11, 59, 13, 424454, tzinfo=datetime.timezone.utc))),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
