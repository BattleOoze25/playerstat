# Generated by Django 4.2 on 2023-04-24 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_score_match'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='match',
        ),
    ]
