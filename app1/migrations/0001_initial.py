# Generated by Django 2.0.13 on 2022-11-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nobel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sTitle', models.CharField(max_length=250)),
                ('sIndex', models.CharField(max_length=100)),
                ('sAbstract', models.CharField(max_length=250)),
                ('tPublish', models.DateTimeField()),
            ],
        ),
    ]