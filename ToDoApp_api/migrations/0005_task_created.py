# Generated by Django 2.2 on 2024-02-04 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp_api', '0004_task_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
