# Generated by Django 2.1 on 2018-08-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intentengine', '0002_auto_20180824_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='provisioningstatus',
            name='provisionTaskId',
            field=models.IntegerField(default=0),
        ),
    ]
