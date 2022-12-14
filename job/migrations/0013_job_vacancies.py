# Generated by Django 4.0.2 on 2022-06-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_daily_opportunie_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='media')),
                ('job_description', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=300)),
            ],
        ),
    ]
