# Generated by Django 4.2.2 on 2023-06-18 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_operation'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='draw_id',
        ),
        migrations.AlterField(
            model_name='operation_status',
            name='user_id_Operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Operation', to='api.account'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
