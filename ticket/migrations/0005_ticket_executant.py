# Generated by Django 4.1.6 on 2023-06-23 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0004_department_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='executant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executans', to=settings.AUTH_USER_MODEL),
        ),
    ]
