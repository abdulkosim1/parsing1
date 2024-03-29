# Generated by Django 4.1.6 on 2023-06-25 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0005_ticket_executant'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfflineTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True)),
                ('status', models.BooleanField(default=True)),
                ('activation_code', models.CharField(blank=True, max_length=7, unique=True)),
                ('number', models.CharField(blank=True, max_length=6, unique=True)),
                ('executant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executans_1', to=settings.AUTH_USER_MODEL)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_1', to='ticket.transaction')),
            ],
        ),
    ]
