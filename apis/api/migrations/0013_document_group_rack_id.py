# Generated by Django 4.2.2 on 2023-07-02 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_borrowing_user_id_borrowing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='group_rack_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.rack_group'),
        ),
    ]
