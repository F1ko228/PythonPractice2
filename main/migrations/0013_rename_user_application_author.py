# Generated by Django 4.2.5 on 2023-11-21 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_application_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='user',
            new_name='author',
        ),
    ]