# Generated by Django 5.1 on 2024-09-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0019_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='XLink',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='fbookLink',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='instaLink',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='linkedInLink',
            field=models.CharField(default='', max_length=100),
        ),
    ]
