# Generated by Django 3.1.5 on 2021-01-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='parent_email',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='parent_name',
            new_name='parent_first_name',
        ),
        migrations.AddField(
            model_name='student',
            name='parent_last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]
