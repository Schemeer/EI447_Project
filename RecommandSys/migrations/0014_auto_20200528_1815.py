# Generated by Django 3.0.6 on 2020-05-28 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RecommandSys', '0013_auto_20200528_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authorcollectfield',
            old_name='filedid',
            new_name='fieldid',
        ),
        migrations.RenameField(
            model_name='papercollectfield',
            old_name='filedid',
            new_name='fieldid',
        ),
    ]
