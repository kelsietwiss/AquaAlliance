# Generated by Django 4.1.6 on 2023-03-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docmodel',
            name='doc',
            field=models.FileField(upload_to='images/'),
        ),
    ]