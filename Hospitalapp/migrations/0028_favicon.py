# Generated by Django 5.1 on 2024-09-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0027_logo_logo_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='favicon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ImageField(upload_to='icon')),
                ('appletouchicon', models.ImageField(upload_to='icon')),
            ],
        ),
    ]
