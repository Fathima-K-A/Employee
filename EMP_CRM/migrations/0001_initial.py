# Generated by Django 3.2.14 on 2024-04-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_place', models.CharField(max_length=100)),
                ('emp_age', models.CharField(max_length=100)),
                ('emp_position', models.CharField(max_length=100)),
            ],
        ),
    ]
