# Generated by Django 4.2 on 2023-05-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]