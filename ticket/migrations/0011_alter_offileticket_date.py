# Generated by Django 4.1.6 on 2023-06-25 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_alter_offileticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offileticket',
            name='date',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]