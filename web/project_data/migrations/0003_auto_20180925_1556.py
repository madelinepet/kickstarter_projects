# Generated by Django 2.1.1 on 2018-09-25 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_data', '0002_kickstarter_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kickstarter',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='kickstarter',
            name='usd_pledged',
        ),
    ]
