# Generated by Django 3.0.6 on 2020-05-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecommandSys', '0023_parsedaffiliations_shortname'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('affiliationshortname', models.CharField(max_length=20)),
                ('needupdata', models.BooleanField()),
                ('authorid0', models.PositiveIntegerField()),
                ('authorid1', models.PositiveIntegerField()),
                ('authorid2', models.PositiveIntegerField()),
                ('authorid3', models.PositiveIntegerField()),
                ('authorid4', models.PositiveIntegerField()),
                ('authorid5', models.PositiveIntegerField()),
                ('authorid6', models.PositiveIntegerField()),
                ('authorid7', models.PositiveIntegerField()),
                ('authorid8', models.PositiveIntegerField()),
                ('authorid9', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['username', 'affiliationshortname'],
            },
        ),
    ]
