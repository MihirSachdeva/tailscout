# Generated by Django 3.1 on 2020-10-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailscout_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='bacteria',
            field=models.CharField(choices=[('B1', 'Bacteria_1'), ('B1', 'Bacteria_1'), ('B1', 'Bacteria_1')], max_length=2),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('B1', 'Bacteria_1'), ('B1', 'Bacteria_1'), ('B1', 'Bacteria_1')], max_length=2),
        ),
    ]