# Generated by Django 4.0.2 on 2022-04-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='role',
            field=models.CharField(max_length=100, null=True),
        ),
    ]