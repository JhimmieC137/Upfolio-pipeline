# Generated by Django 4.0.2 on 2022-07-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0023_remove_programs_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='description',
            field=models.TextField(max_length=700, null=True),
        ),
    ]
