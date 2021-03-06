# Generated by Django 2.2.5 on 2019-10-25 19:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=70, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('gender', models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(3)])),
                ('bio', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
