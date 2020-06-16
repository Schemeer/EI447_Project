# Generated by Django 3.0.6 on 2020-05-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecommandSys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['c_time'], 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AddField(
            model_name='userinfo',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]