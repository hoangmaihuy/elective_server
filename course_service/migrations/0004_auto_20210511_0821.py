# Generated by Django 3.2 on 2021-05-11 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_service', '0003_auto_20210511_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='review_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='review_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
