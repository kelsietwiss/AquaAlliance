# Generated by Django 4.1.6 on 2023-03-09 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_of',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
