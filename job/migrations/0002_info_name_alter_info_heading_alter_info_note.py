# Generated by Django 4.0.2 on 2022-02-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='heading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
