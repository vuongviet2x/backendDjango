# Generated by Django 4.2.2 on 2023-07-07 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_borrowing_user_id_borrowing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='rack_id_Operation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.rack'),
        ),
    ]
