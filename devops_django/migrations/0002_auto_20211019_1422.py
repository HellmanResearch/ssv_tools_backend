# Generated by Django 3.2.8 on 2021-10-19 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('devops_django', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lock',
            name='create_time',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AddField(
            model_name='lock',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
