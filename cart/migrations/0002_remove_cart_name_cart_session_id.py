# Generated by Django 5.1 on 2024-09-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
