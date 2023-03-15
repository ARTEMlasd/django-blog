# Generated by Django 4.1.3 on 2022-12-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField()),
                ('comment', models.TextField(default='None')),
                ('date', models.IntegerField()),
                ('views', models.IntegerField()),
                ('text', models.TextField(default='None')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='None')),
                ('nic', models.TextField(default='None')),
                ('password', models.TextField(default='int')),
                ('mail', models.TextField(default='None')),
            ],
        ),
    ]
