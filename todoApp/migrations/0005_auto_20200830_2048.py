# Generated by Django 3.0.8 on 2020-08-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0004_auto_20200830_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='storyPoints',
            field=models.PositiveIntegerField(),
        ),
    ]
