# Generated by Django 4.1.5 on 2023-01-25 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicpost',
            name='songs',
        ),
        migrations.AddField(
            model_name='musicpost',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='musicstat',
            name='play_count',
            field=models.IntegerField(null=True),
        ),
    ]