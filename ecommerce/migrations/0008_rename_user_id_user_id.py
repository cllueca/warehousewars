# Generated by Django 4.1.1 on 2023-03-05 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_user_telefono'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='user_id',
        ),
    ]
