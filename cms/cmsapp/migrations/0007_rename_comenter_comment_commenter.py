# Generated by Django 3.2.18 on 2023-04-11 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comenter',
            new_name='commenter',
        ),
    ]
