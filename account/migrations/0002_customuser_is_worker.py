# Generated by Django 4.1.6 on 2023-06-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_worker',
            field=models.BooleanField(default=False),
        ),
    ]
