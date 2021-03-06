# Generated by Django 3.0.6 on 2020-05-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecommandSys', '0010_auto_20200526_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='CUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='CUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='CUTeAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='CUTeParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='ECNUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='ECNUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='FUDANAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='FUDANParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='HUSTAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='HUSTParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='LONDONAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='LONDONParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='MITAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='MITParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='NJUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='NJUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='NTUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='NTUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='PKUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='PKUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SCUTAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SCUTParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SEUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SEUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SJTUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SJTUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SYSUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SYSUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SZUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='SZUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='THUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='THUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='TONGJIAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='TONGJIParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='UTAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='UTParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='WHUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='WHUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='ZJUAuthorField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('field_id1', models.PositiveIntegerField()),
                ('weight1', models.FloatField()),
                ('field_id2', models.PositiveIntegerField()),
                ('weight2', models.FloatField()),
                ('field_id3', models.PositiveIntegerField()),
                ('weight3', models.FloatField()),
                ('field_id4', models.PositiveIntegerField()),
                ('weight4', models.FloatField()),
                ('field_id5', models.PositiveIntegerField()),
                ('weight5', models.FloatField()),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='ZJUParentField',
            fields=[
                ('author_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('parents', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
    ]
