# Generated by Django 3.0.8 on 2020-08-30 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_task_storypoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='action',
            field=models.TextField(),
        ),
    ]
