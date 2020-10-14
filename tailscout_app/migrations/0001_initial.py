# Generated by Django 3.1 on 2020-10-14 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bacteria', models.CharField(choices=[('S1', 'Step_1'), ('S2', 'Step_2'), ('S3', 'Step_3')], max_length=2)),
                ('email_id', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('S1', 'Step_1'), ('S2', 'Step_2'), ('S3', 'Step_3')], max_length=2)),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]