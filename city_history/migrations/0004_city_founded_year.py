# Generated by Django 2.2.9 on 2020-02-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_history', '0003_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='founded_year',
            field=models.IntegerField(default=0),
        ),
    ]
