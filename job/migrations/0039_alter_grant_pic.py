# Generated by Django 4.0.2 on 2022-08-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0038_alter_projects_description1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='pic',
            field=models.ImageField(upload_to='statics'),
        ),
    ]