# Generated by Django 3.0.6 on 2020-05-24 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecommandSys', '0005_auto_20200523_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmPaper',
            fields=[
                ('paper_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=2500)),
                ('doi', models.CharField(max_length=200)),
                ('year', models.PositiveSmallIntegerField()),
                ('doc_type', models.PositiveIntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('journal_id', models.PositiveIntegerField()),
                ('conference_series_id', models.PositiveIntegerField()),
                ('conference_instance_id', models.PositiveIntegerField()),
                ('volume', models.SmallIntegerField()),
                ('issue', models.SmallIntegerField()),
                ('first_page', models.SmallIntegerField()),
                ('last_page', models.SmallIntegerField()),
                ('created_at', models.PositiveIntegerField()),
                ('updated_at', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'am_paper',
                'managed': False,
            },
        ),
    ]
