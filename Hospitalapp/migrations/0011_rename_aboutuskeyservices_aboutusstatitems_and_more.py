# Generated by Django 5.1 on 2024-09-05 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0010_aboutus_aboutuskeyservices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutUsKeyServices',
            new_name='AboutUsStatitems',
        ),
        migrations.RenameField(
            model_name='aboutusstatitems',
            old_name='kservice_desc',
            new_name='statitems_desc',
        ),
        migrations.RenameField(
            model_name='aboutusstatitems',
            old_name='kservice_icon',
            new_name='statitems_icon',
        ),
        migrations.RenameField(
            model_name='aboutusstatitems',
            old_name='kservice_title',
            new_name='statitems_title',
        ),
    ]
