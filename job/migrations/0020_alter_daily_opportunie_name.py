# Generated by Django 4.0.2 on 2022-06-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0019_competition_fellowship_grant_internship_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_opportunie',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
