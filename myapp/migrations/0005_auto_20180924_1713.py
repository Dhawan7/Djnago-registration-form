# Generated by Django 2.1.1 on 2018-09-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_ajax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ajax',
            name='email',
        ),
        migrations.AddField(
            model_name='ajax',
            name='password',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
