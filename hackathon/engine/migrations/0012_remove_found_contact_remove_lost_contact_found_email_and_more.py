# Generated by Django 4.1.4 on 2023-01-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0011_found_lost_delete_engine_other_delete_engine_own'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='found',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='lost',
            name='contact',
        ),
        migrations.AddField(
            model_name='found',
            name='email',
            field=models.CharField(default='', max_length=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lost',
            name='email',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]