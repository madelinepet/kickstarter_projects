# Generated by Django 2.1.1 on 2018-09-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kickstarter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.CharField(max_length=1024)),
                ('name', models.CharField(max_length=1024)),
                ('category', models.CharField(max_length=1024)),
                ('main_category', models.CharField(max_length=1024)),
                ('currency', models.CharField(max_length=1024)),
                ('deadline', models.CharField(max_length=1024)),
                ('goal', models.FloatField()),
                ('launched', models.CharField(max_length=1024)),
                ('pledged', models.FloatField()),
                ('state', models.CharField(max_length=1024)),
                ('backers', models.IntegerField()),
                ('country', models.CharField(max_length=1024)),
                ('usd_pledged', models.FloatField()),
                ('usd_pledged_real', models.FloatField()),
                ('usd_goal_real', models.FloatField()),
            ],
        ),
    ]
