# Generated by Django 5.1 on 2024-09-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0022_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title_position', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='img_testimonial')),
                ('rating', models.IntegerField()),
                ('content', models.TextField()),
            ],
        ),
    ]
