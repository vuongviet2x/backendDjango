# Generated by Django 2.2 on 2023-05-16 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230515_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_light', models.CharField(max_length=20)),
                ('ventilate', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField()),
                ('rack_id_Operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Rack')),
            ],
        ),
    ]