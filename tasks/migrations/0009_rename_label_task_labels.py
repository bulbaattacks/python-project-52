# Generated by Django 4.2 on 2023-05-11 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_remove_task_assignee_task_executor_alter_task_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='label',
            new_name='labels',
        ),
    ]
