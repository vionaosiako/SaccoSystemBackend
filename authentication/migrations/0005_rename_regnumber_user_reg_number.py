# Generated by Django 4.1 on 2022-10-19 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_reg_number_user_regnumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='regnumber',
            new_name='reg_number',
        ),
    ]