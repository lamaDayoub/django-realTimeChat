# Generated by Django 5.2.1 on 2025-06-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmessage',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
