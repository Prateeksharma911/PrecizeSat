# Generated by Django 2.2.11 on 2023-05-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('sat_score', models.FloatField()),
            ],
        ),
    ]
