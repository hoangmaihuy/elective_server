# Generated by Django 3.2 on 2021-04-19 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_superuser', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('last_login', models.PositiveBigIntegerField()),
                ('create_time', models.PositiveBigIntegerField()),
            ],
            options={
                'db_table': 'user_tab',
            },
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['email'], name='email_idx'),
        ),
    ]
