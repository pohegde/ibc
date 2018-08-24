# Generated by Django 2.1 on 2018-08-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branchxmlfiles',
            fields=[
                ('pkid', models.AutoField(primary_key=True, serialize=False)),
                ('template', models.IntegerField()),
                ('xml', models.CharField(max_length=2000)),
                ('datecreated', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('pkid', models.AutoField(primary_key=True, serialize=False)),
                ('intent', models.CharField(max_length=2000)),
                ('submittime', models.DateField()),
                ('status', models.CharField(max_length=2000)),
            ],
        ),
    ]