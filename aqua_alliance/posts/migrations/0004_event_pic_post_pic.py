# Generated by Django 4.1.6 on 2023-03-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_event_date_of'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
