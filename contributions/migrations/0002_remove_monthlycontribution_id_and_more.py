# Generated by Django 4.1 on 2022-10-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlycontribution',
            name='id',
        ),
        migrations.AlterField(
            model_name='monthlycontribution',
            name='receipt_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
