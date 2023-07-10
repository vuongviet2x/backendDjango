# Generated by Django 4.2.2 on 2023-06-25 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_document_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='handlemoving',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operation',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='guide_light',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operation',
            name='ventilate',
            field=models.IntegerField(default=0),
        ),
    ]