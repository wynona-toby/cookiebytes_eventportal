# Generated by Django 5.0.2 on 2024-02-25 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_event_cost_event_days_event_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='highlights',
        ),
        migrations.AddField(
            model_name='event',
            name='highlight_event',
            field=models.TextField(default=12345),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
    ]
