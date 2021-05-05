# Generated by Django 3.2 on 2021-05-05 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('course_id', models.PositiveBigIntegerField()),
                ('teacher_id', models.PositiveBigIntegerField()),
                ('semester', models.PositiveSmallIntegerField()),
                ('review_count', models.PositiveSmallIntegerField()),
                ('create_time', models.PositiveBigIntegerField()),
            ],
            options={
                'db_table': 'class_tab',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('course_no', models.CharField(max_length=50)),
                ('credit', models.PositiveSmallIntegerField()),
                ('school_id', models.PositiveSmallIntegerField()),
                ('type', models.PositiveSmallIntegerField()),
                ('review_count', models.PositiveIntegerField()),
                ('last_review', models.PositiveBigIntegerField()),
                ('create_time', models.PositiveBigIntegerField()),
            ],
            options={
                'db_table': 'course_tab',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('review_count', models.PositiveIntegerField()),
                ('create_time', models.PositiveBigIntegerField()),
            ],
            options={
                'db_table': 'teacher_tab',
            },
        ),
        migrations.AddIndex(
            model_name='teacher',
            index=models.Index(fields=['name'], name='teacher_name_idx'),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['name'], name='course_name_idx'),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['course_no'], name='course_no_idx'),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['school_id'], name='school_id_idx'),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['type'], name='course_type_idx'),
        ),
        migrations.AddIndex(
            model_name='class',
            index=models.Index(fields=['course_id'], name='course_id_idx'),
        ),
    ]