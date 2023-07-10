# Generated by Django 4.2.2 on 2023-06-30 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_borrowing_user_id_borrowing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='user_id_Borrowing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Borrowing', to='api.account'),
        ),
        migrations.AlterField(
            model_name='breakdown_status',
            name='rack_id_Breakdown',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Beakdown', to='api.account'),
        ),
        migrations.AlterField(
            model_name='document',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='operation_status',
            name='user_id_Operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Operation', to='api.account'),
        ),
        migrations.AlterField(
            model_name='rack',
            name='user_id_Rack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Rack', to='api.account'),
        ),
        migrations.AlterField(
            model_name='rack_group',
            name='user_id_Rackgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Rack_group', to='api.account'),
        ),
    ]
