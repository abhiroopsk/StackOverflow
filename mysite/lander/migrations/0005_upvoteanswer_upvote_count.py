# Generated by Django 3.0.6 on 2021-10-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lander', '0004_auto_20211019_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='upvoteanswer',
            name='upvote_count',
            field=models.IntegerField(default=0),
        ),
    ]
