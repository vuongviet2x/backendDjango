# Generated by Django 2.2 on 2023-05-15 07:22

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rack_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id_Rackgroup', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rack_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Rack_group')),
                ('user_id_Rack', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Operation_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_speed', models.FloatField()),
                ('weight', models.FloatField()),
                ('displacement', models.FloatField()),
                ('number_users', models.IntegerField()),
                ('is_hard_locked', models.BooleanField(default=False)),
                ('is_endpoint', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('rack_id_Operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Rack')),
                ('user_id_Operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Environment_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('smoke', models.CharField(max_length=100)),
                ('collision', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('rack_id_Environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Rack')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('published_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('rack_id_Document', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Rack')),
                ('user_id_Document', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Breakdown_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_obstructed', models.BooleanField(default=False)),
                ('is_skewed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_overload_motor', models.BooleanField(default=False)),
                ('rack_id_Breakdown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Rack')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_borrowed', models.DateTimeField()),
                ('date_returned', models.DateTimeField()),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Document')),
                ('user_id_Borrowing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Account')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(upload_to='uploads/%Y/%m')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
