# Generated by Django 3.0.6 on 2020-05-24 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RecommandSys', '0007_auto_20200524_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='affiliationcollect',
            old_name='conutry',
            new_name='country',
        ),
    ]