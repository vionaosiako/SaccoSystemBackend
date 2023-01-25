# Generated by Django 4.1 on 2023-01-25 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loans', '0005_loanrequest_payment_period_years'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_loan', models.PositiveIntegerField(default=0)),
                ('payable_loan', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
