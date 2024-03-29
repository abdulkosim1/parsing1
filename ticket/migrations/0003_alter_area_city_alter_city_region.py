# Generated by Django 4.1.6 on 2023-06-23 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_remove_area_region_remove_city_area_area_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='ticket.city'),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='ticket.region'),
        ),
    ]
