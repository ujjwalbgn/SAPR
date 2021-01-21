# Generated by Django 3.1.5 on 2021-01-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_auto_20210121_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='classattendance',
            name='Class_type',
            field=models.CharField(choices=[('In person', 'In person'), ('Online', 'Online')], default='In Person', max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='7099', max_length=4, unique=True),
        ),
    ]