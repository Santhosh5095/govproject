# Generated by Django 4.2.5 on 2023-09-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_rename_status_pipeline_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]