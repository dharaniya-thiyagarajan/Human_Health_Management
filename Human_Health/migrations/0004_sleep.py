# Generated by Django 5.0.4 on 2024-04-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Human_Health', '0003_water'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
            ],
        ),
    ]
