# Generated by Django 3.0.6 on 2020-05-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecommandSys', '0004_auto_20200523_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliationcollect',
            name='affiliationid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='authorcollect',
            name='authorid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='papercollect',
            name='paperid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='papercollect',
            name='year',
            field=models.IntegerField(),
        ),
    ]