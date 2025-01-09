# Generated by Django 5.1.4 on 2025-01-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_person_age_person_city_person_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('city', models.CharField(default='city', max_length=100)),
            ],
        ),
    ]
