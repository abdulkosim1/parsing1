# Generated by Django 4.1.6 on 2023-06-29 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0016_offileticket_queue_id_offileticket_queue_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offileticket',
            name='queue_id',
        ),
        migrations.RemoveField(
            model_name='offileticket',
            name='queue_type',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='queue_id',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='queue_type',
        ),
        migrations.DeleteModel(
            name='Queue',
        ),
    ]
