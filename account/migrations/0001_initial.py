# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0005_alter_user_last_login_null'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(max_length=20, verbose_name='username', unique=True, help_text='An alpha-numeric identifier for an account.', validators=[django.core.validators.RegexValidator(regex='[a-zA-Z0-9]+', message='Please use only alpha-numeric characters.')])),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail', unique=True, help_text='An e-mail address.')),
                ('display_name', models.CharField(max_length=48, verbose_name='display name', unique=True, help_text='Name shown to other users.')),
                ('personal_name', models.CharField(max_length=64, blank=True, help_text="Optional; a user's personal name.", verbose_name='personal name')),
                ('location', models.CharField(max_length=64, blank=True, help_text="Optional; a user's location.", verbose_name='location')),
                ('birth_date', models.DateField(blank=True, help_text="Optional; a user's birthday.", verbose_name='birth date', null=True)),
                ('gender', models.CharField(max_length=32, blank=True, help_text="Optional; a phrase representing a user's gender.", verbose_name='gender')),
                ('pronouns', models.CharField(max_length=2, choices=[('n', 'Neutral (they, them, their, theirs)'), ('m', 'Male (he, him, his)'), ('f', 'Female (she, her, hers)')], help_text='Pronouns to use to refer to the user.', verbose_name='pronouns')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Deselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(to='auth.Group', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', blank=True, related_query_name='user')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', related_name='user_set', help_text='Specific permissions for this user.', verbose_name='user permissions', blank=True, related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
