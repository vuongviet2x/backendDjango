# Generated by Django 4.2.2 on 2023-06-23 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_document_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='user_id_Document',
        ),
    ]
